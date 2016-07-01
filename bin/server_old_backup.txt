// Copyright (c) 2016, <your name>. All rights reserved. Use of this source code
// is governed by a BSD-style license that can be found in the LICENSE file.

import 'dart:io';
import 'dart:async';
import 'package:http_server/http_server.dart';

import 'package:args/args.dart';
import 'package:shelf/shelf.dart' as shelf;
import 'package:shelf/shelf_io.dart' as io;
import 'package:shelf_route/shelf_route.dart';
import 'dart:convert';
import 'package:shelf/src/response.dart';
import 'package:mime/mime.dart';

void main(List<String> args) {
  var myRouter = router()
    ..get('/', (_) => new Response.ok("Hello World"),
        middleware: shelf.logRequests())
    ..put('/base64toJson/', (request) => B64toJsonHandler(request),
        middleware: shelf.logRequests());

  printRoutes(myRouter);

  var parser = new ArgParser()
    ..addOption('port', abbr: 'p', defaultsTo: '8088');

  var result = parser.parse(args);

  var port = int.parse(result['port'], onError: (val) {
    stdout.writeln('Could not parse port value "$val" into a number.');
    exit(1);
  });

  //
  // var handler = const shelf.Pipeline()
  //     .addMiddleware(shelf.logRequests())
  //     .addHandler(_echoRequest);

  io.serve(myRouter.handler, 'localhost', port).then((server) {
    print('Serving at http://${server.address.host}:${server.port}');
  });
}

B64toJsonHandler(HttpRequest request) {
  print("B64 handler");
  String boundary = request.headers.contentType.parameters['boundary'];
  request
    .transform(new MimeMultipartTransformer(boundary))
    .map(HttpMultipartFormData.parse)
    .map((HttpMultipartFormData formData) {
       var file = formData.value("file");
       print ("FileContent: $file");
      // form data object available here.
    });

  return new Response.ok("B64 handler called");
}

Future<shelf.Response> _echoRequest(shelf.Request request) async {
  String s = await request.readAsString();
  print("Request URL: ${request.url}");
  print("Request Mime Type: ${request.mimeType}");
  print("Request: $s");
  await executeCommand(".\\temp\\convert.py", [request.url.toString()]);
  return new shelf.Response.ok('Request for "${request.url}" and $s ');
}

Future executeCommand(String command, List<String> attributes) async {
  Process process = await Process.start(command, attributes, runInShell: true);
  var lineStream = process.stdout.transform(new Utf8Decoder());
  await for (var l in lineStream) {
    print(l);
  }
  process.stderr.drain();
  print('exit code: ${await process.exitCode}');
  return;
}

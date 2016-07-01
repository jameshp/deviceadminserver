import 'dart:async';
import 'dart:io';
import 'dart:convert';

import 'package:rpc/rpc.dart';

class SimpleMessage {
  String field1;
  String field2;
}

class AppConfigMessage {
  MediaMessage appConfig;
}

class AppConfigResponse{
  Map<String,String> appConfigJson;
}

class MegaMixMessage {
  String name;
  int age;
  MediaMessage resume;
}

class MultipleFile {
  List<MediaMessage> files;
}

class MultipleFile2 {
  Map<String, MediaMessage> files;
}

class TestMessage{
  String bla;
}

@ApiClass(version: 'v1',
          name:'appconfigapi')
class AppConfigAPI {
  @ApiResource()
  PostAPI post = new PostAPI();
}

class PostAPI {
  @ApiMethod(path: 'test/', method: 'GET')
  TestMessage getTest(){
    return new TestMessage()
                ..bla = "Hello World";
  }

  @ApiMethod(path: 'post/simple', method: 'POST')
  SimpleMessage test1(SimpleMessage message) {
    return message;
  }

  @ApiMethod(path: 'appconfig', method: 'POST')
  Future<AppConfigResponse> returnAppConfig(AppConfigMessage message) async{
    //var appConfig = message.appConfig.toString();
    String b64_message = UTF8.decode(message.appConfig.bytes);
    List<int> dat_message = BASE64.decode(b64_message);
    File datFile = new File("temp.dat");
    datFile.writeAsBytes(dat_message);

    //print (b64_message);
    await executeCommand("dat2json.bat",[]);

    File jsonFile = new File('temp.json');
    String mapAsJson = await jsonFile.readAsString();
     //app_cfg.py spbt_config CONVERT spbt_config.json -o spbt_config.dat
      //app_cfg.py event CONVERT c:/temp/new_event.dat -o c:/temp/converted_event.js --in-format dat --out-format json

    Map parsedMap = JSON.decode(mapAsJson);
    jsonFile.delete();
    // File datFile = new File('temp.dat');
    // datFile.delete();

    AppConfigResponse r = new AppConfigResponse();
    r.appConfigJson = parsedMap;
    return r;
  }

  @ApiMethod(path: 'post/mega-mix', method: 'POST')
  MegaMixMessage test3(MegaMixMessage message) {
    return message;
  }

  @ApiMethod(path: 'post/collection/list', method: 'POST')
  MultipleFile test4(MultipleFile message) {
    return message;
  }

  @ApiMethod(path: 'post/collection/map', method: 'POST')
  MultipleFile2 test5(MultipleFile2 message) {
    return message;
  }
}

Future main() async {
  ApiServer _apiServer = new ApiServer(apiPrefix: '', prettyPrint: true);
  _apiServer.enableDiscoveryApi();
  _apiServer.addApi(new AppConfigAPI());

  final server = await HttpServer.bind(InternetAddress.ANY_IP_V4, 4242);
  server.listen((HttpRequest request) {
    _apiServer.httpRequestHandler(request);
  });
}


Future executeCommand(String command, List<String> attributes) async {
  print ("command: $command");
  print ("args: $attributes");
  Process process = await Process.start(command, attributes, runInShell: true);
  var lineStream = process.stdout.transform(new Utf8Decoder());
  await for (var l in lineStream) {
    print(l);
  }
  process.stderr.drain();
  print('exit code: ${await process.exitCode}');
  return;
}

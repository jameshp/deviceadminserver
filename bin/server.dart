import 'dart:async';
import 'dart:io';
import 'dart:convert';

import 'package:rpc/rpc.dart';

//reprsents the app config in base64 Fromat to be converted
class AppConfigMessage {
  String fileName;
  String fileSize;
  MediaMessage appConfig;
}

//represents the app config in json format
class AppConfigResponse {
  Map<String, String> appConfigJson;
}

class AppConfigBase64EncodedResponse {
  String base64AppConfig;
}

class TestMessage {
  String bla;
}

@ApiClass(version: 'v1', name: 'appconfigapi')
class AppConfigAPI {
  @ApiResource()
  PostAPI post = new PostAPI();
}

class PostAPI {
  @ApiMethod(path: 'test/', method: 'GET')
  TestMessage getTest() {
    return new TestMessage()..bla = "Hello World";
  }

  @ApiMethod(path: 'appconfig', method: 'POST')
  Future<AppConfigResponse> returnAppConfig(AppConfigMessage message) async {
    //var appConfig = message.appConfig.toString();
    String b64_message = UTF8.decode(message.appConfig.bytes);
    List<int> dat_message = BASE64.decode(b64_message);
    File datFile = new File("temp.dat");
    await datFile.writeAsBytes(dat_message);

    //print (b64_message);
    if (Platform.isLinux){
        await executeCommand("/app/dat2json.sh", []);
    }
    if (Platform.isWindows){
       await executeCommand("dat2json.bat", []);
    }

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

  @ApiMethod(path: 'json2base64', method: 'POST')
  Future<AppConfigBase64EncodedResponse> returnBase64AppConfig(
      AppConfigMessage message) async {
    File jsonFile = new File("temp_json2dat.json");
    await jsonFile.writeAsBytes(message.appConfig.bytes);
    Map exitCondition;
    if (Platform.isLinux){
        exitCondition = await executeCommand("/app/json2dat.sh", []);
    }
    if (Platform.isWindows){
      exitCondition = await executeCommand("json2dat.bat", []);
    }


    if (exitCondition['exitCode'] != 0){
      throw new RpcError(500, 'json to .dat conversion error', 'expected json input file could not be converted to .dat file')
        ..errors.add(new RpcErrorDetail(reason: exitCondition['reason'] ));
    }

    File datFile = new File("temp_json2dat.dat");
    String base64 = BASE64.encode(datFile.readAsBytesSync());
    AppConfigBase64EncodedResponse r = new AppConfigBase64EncodedResponse()
      ..base64AppConfig = base64;
    return r;
  }
}

Future main() async {
  ApiServer _apiServer = new ApiServer(apiPrefix: '', prettyPrint: true);
  _apiServer.enableDiscoveryApi();
  _apiServer.addApi(new AppConfigAPI());

  final server = await HttpServer.bind(InternetAddress.ANY_IP_V4, 8080);
  server.listen((HttpRequest request) {
    _apiServer.httpRequestHandler(request);
  });
}

Future executeCommand(String command, List<String> attributes) async {
  print("command: $command");
  print("args: $attributes");
  Process process = await Process.start(command, attributes, runInShell: true);
  var lineStream = process.stdout.transform(new Utf8Decoder());
  await for (var l in lineStream) {
    print(l);
  }

  var errorStream = process.stderr.transform(new Utf8Decoder());
  var error = "";
  await for (var e in errorStream){
    print (e);
    error += e;
  }

  //process.stderr.drain();
  print('exit code: ${await process.exitCode}');
  return {'exitCode': await process.exitCode, 'reason': error} ;
}

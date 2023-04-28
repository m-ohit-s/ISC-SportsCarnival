from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    "input_file_location": "C:\\Users\\mohit.sadhwani\\Desktop\\TeamsInputJSON.json",
    "file_format": "json",
    "output_file_location": "C:\\Users\\mohit.sadhwani\\Desktop\\TeamListOuput.json",
    "sql_database_driver_name": "SQL SERVER",
    "server_name": "ITT-MOHITSA",
    "database_name": "LearnAndCode",
    "hostname": "ITT-MOHITSA",
    "port": 5000,
    "size": 1024,
    "format": "utf-8",
    "disconnect_msg": "close",


    "default_command_pattern": r'isc -a (?P<action>\w+) -i (?P<json_input_file>\'[^\']+\') -o ('
                               r'?P<json_output_file>\'[^\']+\')',
    "help_command": r'isc\s+--help',
    "exit_client": "quit"
}

config["LOGGING"] = {
    "filename": "isc.log",
    "filemode": "a",
    # "file_format": '%(asctime)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d]'
}

with open("configurations.ini", "w") as f:
    config.write(f)

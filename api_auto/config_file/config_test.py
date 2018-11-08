class ConIni:
    PPD = {
        "test": {
            "host": "",
            "port": "",
            "header": {"Content-Type":"application/json",}
        },
        "prd": {
                "host": "",
                "port": "",
                "header": {"Content-Type": "application/x-www-form-urlencoded"}
            }
    }
    PPD_2 = {
        "test": {
            "host": "http://localhost",
            "port": "8008",
            "header": {"Content-Type": "application/x-www-form-urlencoded"}
        },
        "prd": {
            "host": "",
            "port": "",
            "header": {"Content-Type": "application/x-www-form-urlencoded"}
        }
    }
# Write your code here
# Write your code here
import json
import re
from datetime import time

"""
data from 1/6
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
]
"""

"""
[     {         "bus_id": 128,         "stop_id": 1,         "stop_name": "Prospekt Avenue",         "next_stop": 3,         "stop_type": "S",         "a_time": 8.12     },     {         "bus_id": 128,         "stop_id": 3,         "stop_name": "",         "next_stop": 5,         "stop_type": "",         "a_time": "08:19"     },     {         "bus_id": 128,         "stop_id": 5,         "stop_name": "Fifth Avenue",         "next_stop": 7,         "stop_type": "O",         "a_time": "08:25"     },     {         "bus_id": 128,         "stop_id": "7",         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:37"     },     {         "bus_id": "",         "stop_id": 2,         "stop_name": "Pilotow Street",         "next_stop": 3,         "stop_type": "S",         "a_time": ""     },     {         "bus_id": 256,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 6,         "stop_type": "",         "a_time": "09:45"     },     {         "bus_id": 256,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 7,         "stop_type": "",         "a_time": "09:59"     },     {         "bus_id": 256,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": "0",         "stop_type": "F",         "a_time": "10:12"     },     {         "bus_id": 512,         "stop_id": 4,         "stop_name": "Bourbon Street",         "next_stop": 6,         "stop_type": "S",         "a_time": "08:13"     },     {         "bus_id": "512",         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 0,         "stop_type": 5,         "a_time": "08:16"     } ]
"""

"""
data from 2/6
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Av.",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "8:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "OO",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:77"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "A",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10.12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "bourbon street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "38:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
[     {         "bus_id": 128,         "stop_id": 1,         "stop_name": "Prospekt Av.",         "next_stop": 3,         "stop_type": "S",         "a_time": "08:12"     },     {         "bus_id": 128,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 5,         "stop_type": "",         "a_time": "8:19"     },     {         "bus_id": 128,         "stop_id": 5,         "stop_name": "Fifth Avenue",         "next_stop": 7,         "stop_type": "OO",         "a_time": "08:25"     },     {         "bus_id": 128,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:77"     },     {         "bus_id": 256,         "stop_id": 2,         "stop_name": "Pilotow Street",         "next_stop": 3,         "stop_type": "S",         "a_time": "09:20"     },     {         "bus_id": 256,         "stop_id": 3,         "stop_name": "Elm",         "next_stop": 6,         "stop_type": "",         "a_time": "09:45"     },     {         "bus_id": 256,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 7,         "stop_type": "A",         "a_time": "09:59"     },     {         "bus_id": 256,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "10.12"     },     {         "bus_id": 512,         "stop_id": 4,         "stop_name": "bourbon street",         "next_stop": 6,         "stop_type": "S",         "a_time": "38:13"     },     {         "bus_id": 512,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:16"     } ]
test case 3 of part 2
[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "abbey Road", "next_stop" : 5, "stop_type" : "FF", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "two"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street Str.", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "39:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:95"},  {"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08.13"},  {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "d", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08;44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boullevard", "next_stop" : 17, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "o", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "s", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska St.", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:76"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Av.", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00:00"},  {"bus_id" : 1024, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]

"""

"""
part 3 of 6 
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]

[     {         "bus_id": 128,         "stop_id": 1,         "stop_name": "Prospekt Avenue",         "next_stop": 3,         "stop_type": "S",         "a_time": "08:12"     },     {         "bus_id": 128,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 5,         "stop_type": "",         "a_time": "08:19"     },     {         "bus_id": 128,         "stop_id": 5,         "stop_name": "Fifth Avenue",         "next_stop": 7,         "stop_type": "O",         "a_time": "08:25"     },     {         "bus_id": 128,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:37"     },     {         "bus_id": 256,         "stop_id": 2,         "stop_name": "Pilotow Street",         "next_stop": 3,         "stop_type": "S",         "a_time": "09:20"     },     {         "bus_id": 256,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 6,         "stop_type": "",         "a_time": "09:45"     },     {         "bus_id": 256,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 7,         "stop_type": "",         "a_time": "09:59"     },     {         "bus_id": 256,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "10:12"     },     {         "bus_id": 512,         "stop_id": 4,         "stop_name": "Bourbon Street",         "next_stop": 6,         "stop_type": "S",         "a_time": "08:13"     },     {         "bus_id": 512,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:16"     } ]
"""

"""
part 4 of 6
************
ex1:
[     {         "bus_id": 128,         "stop_id": 1,         "stop_name": "Prospekt Avenue",         "next_stop": 3,         "stop_type": "S",         "a_time": "08:12"     },     {         "bus_id": 128,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 5,         "stop_type": "",         "a_time": "08:19"     },     {         "bus_id": 128,         "stop_id": 5,         "stop_name": "Fifth Avenue",         "next_stop": 7,         "stop_type": "O",         "a_time": "08:25"     },     {         "bus_id": 128,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:37"     },     {         "bus_id": 512,         "stop_id": 4,         "stop_name": "Bourbon Street",         "next_stop": 6,         "stop_type": "",         "a_time": "08:13"     },     {         "bus_id": 512,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:16"     } ]

ex2:
[     {         "bus_id": 128,         "stop_id": 1,         "stop_name": "Prospekt Avenue",         "next_stop": 3,         "stop_type": "S",         "a_time": "08:12"     },     {         "bus_id": 128,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 5,         "stop_type": "",         "a_time": "08:19"     },     {         "bus_id": 128,         "stop_id": 5,         "stop_name": "Fifth Avenue",         "next_stop": 7,         "stop_type": "O",         "a_time": "08:25"     },     {         "bus_id": 128,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:37"     },     {         "bus_id": 256,         "stop_id": 2,         "stop_name": "Pilotow Street",         "next_stop": 3,         "stop_type": "S",         "a_time": "09:20"     },     {         "bus_id": 256,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 6,         "stop_type": "",         "a_time": "09:45"     },     {         "bus_id": 256,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 7,         "stop_type": "",         "a_time": "09:59"     },     {         "bus_id": 256,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "10:12"     },     {         "bus_id": 512,         "stop_id": 4,         "stop_name": "Bourbon Street",         "next_stop": 6,         "stop_type": "S",         "a_time": "08:13"     },     {         "bus_id": 512,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:16"     } ]

"""

"""
part 5 of 6
**********
ex1:
[     {         "bus_id": 128,         "stop_id": 1,         "stop_name": "Prospekt Avenue",         "next_stop": 3,         "stop_type": "S",         "a_time": "08:12"     },     {         "bus_id": 128,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 5,         "stop_type": "",         "a_time": "08:19"     },     {         "bus_id": 128,         "stop_id": 5,         "stop_name": "Fifth Avenue",         "next_stop": 7,         "stop_type": "O",         "a_time": "08:17"     },     {         "bus_id": 128,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:07"     },     {         "bus_id": 256,         "stop_id": 2,         "stop_name": "Pilotow Street",         "next_stop": 3,         "stop_type": "S",         "a_time": "09:20"     },     {         "bus_id": 256,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 6,         "stop_type": "",         "a_time": "09:45"     },     {         "bus_id": 256,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 7,         "stop_type": "",         "a_time": "09:44"     },     {         "bus_id": 256,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "10:12"     },     {         "bus_id": 512,         "stop_id": 4,         "stop_name": "Bourbon Street",         "next_stop": 6,         "stop_type": "S",         "a_time": "08:13"     },     {         "bus_id": 512,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:16"     } ]

ex2:
[     {         "bus_id": 512,         "stop_id": 4,         "stop_name": "Bourbon Street",         "next_stop": 6,         "stop_type": "S",         "a_time": "08:13"     },     {         "bus_id": 512,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:16"     } ]
"""
"""
part6
ex1:
[     {         "bus_id": 128,         "stop_id": 1,         "stop_name": "Prospekt Avenue",         "next_stop": 3,         "stop_type": "S",         "a_time": "08:12"     },     {         "bus_id": 128,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 5,         "stop_type": "O",         "a_time": "08:19"     },     {         "bus_id": 128,         "stop_id": 5,         "stop_name": "Fifth Avenue",         "next_stop": 7,         "stop_type": "O",         "a_time": "08:25"     },     {         "bus_id": 128,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:37"     },     {         "bus_id": 256,         "stop_id": 2,         "stop_name": "Pilotow Street",         "next_stop": 3,         "stop_type": "S",         "a_time": "09:20"     },     {         "bus_id": 256,         "stop_id": 3,         "stop_name": "Elm Street",         "next_stop": 6,         "stop_type": "",         "a_time": "09:45"     },     {         "bus_id": 256,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 7,         "stop_type": "O",         "a_time": "09:59"     },     {         "bus_id": 256,         "stop_id": 7,         "stop_name": "Sesame Street",         "next_stop": 0,         "stop_type": "F",         "a_time": "10:12"     },     {         "bus_id": 512,         "stop_id": 4,         "stop_name": "Bourbon Street",         "next_stop": 6,         "stop_type": "S",         "a_time": "08:13"     },     {         "bus_id": 512,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:16"     } ]
[     {         "bus_id": 512,         "stop_id": 4,         "stop_name": "Bourbon Street",         "next_stop": 6,         "stop_type": "S",         "a_time": "08:13"     },     {         "bus_id": 512,         "stop_id": 6,         "stop_name": "Sunset Boulevard",         "next_stop": 0,         "stop_type": "F",         "a_time": "08:16"     } ]
"""


def load_data(data_str: str) -> list:
    dl = json.loads(data_str)
    return dl


def _init_error_d(key_list) -> dict:
    d = dict()
    for k in key_list:
        d[k] = 0
    return d

def _check_str(value) -> int:
    error = 0
    if type(value) != str:
        error = 1
    else:
        if len(value) == 0:
            error = 1
    return error


def _check_int(value) -> int:
    error = 0
    if type(value) != int:
        error = 1
    return error


def _check_chr(value) -> int:
    error = 0
    # if value not in ['S', 'O', 'F']:
    #     error = 1
    # return error
    if type(value) != str:
        error = 1
    else:
        if len(value) > 1:
            error = 1
    return error

def _check_stop_name(value) -> int:
    # print('>input',value)
    error = 0
    if type(value) != str:
        # print('str', value)
        error = 1
    else:
        if not re.match('[A-Z]', value):
            # print('cap', value)
            error = 1
        if len(value.split(' ')) < 2:
            error = 1
        if value.split(' ')[-1] not in ['Road', 'Avenue', 'Boulevard', 'Street']:
            error = 1
            # print('suffix', value)
    return error

def _check_time_form(value):
    temp = r'^(?:[01]?\d|2[0-3])(?::[0-5]\d){1,2}$'
    temp = r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
    if not re.match(temp, value):
        # print(value)
        return 1
    return 0

def _check_stop_type(value):
    if value not in ['S', 'O', 'F', '']:
        # print(value)
        return 1
    return 0


def _no_check(value) -> int:
    return 0

def check_data(dl):
    data_types = dict()
    # data_types['bus_id'] = _no_check
    # data_types['stop_id'] = _no_check
    data_types['stop_name'] = _check_stop_name
    # data_types['next_stop'] = _no_check
    data_types['stop_type'] = _check_stop_type
    data_types['a_time'] = _check_time_form

    error_d = _init_error_d(list(data_types.keys()))

    for d in dl:
        for k, check_f in data_types.items():
            error = check_f(d[k])
            error_d[k] = error_d[k] + error

    return error_d

def print_output(d):
    total_errors = 0
    for k,v in d.items():
        total_errors = total_errors + v
    print('Format validation: ' + str(total_errors) + ' errors')
    for k,v in d.items():
        print(k + ': '+str(v))


## part 3 ##

def count_stops(dl):
    stop_d = dict()
    for d in dl:
        for k, v in d.items():
            if k == 'bus_id':
                if v in stop_d:
                    stop_d[v] = stop_d[v] + 1
                else:
                    stop_d[v] = 1

    return dict(sorted(stop_d.items()))


def print_stops(stop_d):
    print('Line names and number of stops:')
    for id, stops in stop_d.items():
        print('bus_id: '+str(id) + ', stops: '+str(stops))

### part 4 ###

def count_in_list(l, what):
    count = 0
    for e in l:
        if e == what:
            count = count + 1
    return count

def check_start_stop(dl: list[dict]):
    rd = dict()
    for d in dl:
        if d['bus_id'] in rd:
            rd[d['bus_id']].append(d['stop_type'])
        else:
            rd[d['bus_id']] = [d['stop_type']]

    for bid, s_types in rd.items():
        if count_in_list(s_types, 'S') != 1:
            print('There is no start or end stop for the line: ' + str(bid) + '.')
            return False
        if count_in_list(s_types, 'F') !=1:
            print('There is no start or end stop for the line: ' + str(bid) + '.')
            return False
    return True

def find_trans(stop_l: list):
    rl = []
    s = set(stop_l)
    for e in s:
        count = count_in_list(stop_l, e)
        if count>1:
            rl.append(e)
    return rl


def count_start_stop_and_name(dl: list[dict], print_output=False):
    d_ = dict()
    d_['starts'] = []
    d_['finishes'] = []
    d_['all'] = []
    for d in dl:
        if d['stop_type'] == 'S':
            d_['starts'].append(d['stop_name'])
        if d['stop_type'] == 'F':
            d_['finishes'].append(d['stop_name'])
        d_['all'].append(d['stop_name']) # all

    d_['trans'] = find_trans(d_['all'])

    # sort

    for k,v in d_.items():

        v_set = set(v)
        v_s_l = sorted(list(v_set))
        d_[k] = v_s_l

    if print_output:
        print('Start stops: ' + str(len(d_['starts']))+' '+str(d_['starts']))
        print('Transfer stops: ' + str(len(d_['trans'])) + ' ' + str(d_['trans']))
        print('Finish stops: ' + str(len(d_['finishes'])) + ' ' + str(d_['finishes']))

    return d_


### part 5 ###
def _sort_rout(dl):
    sorted_rout = []
    for i in range(len(dl)):  # find start
        d = dl[i]
        if d['stop_type'] == 'S':
            sorted_rout.append(d)
            dl.pop(i)
            break

    while len(dl) > 2:
        for i in range(len(dl)):
            d = dl[i]
            if d['stop_id'] == sorted_rout[-1]['next_stop']:
                sorted_rout.append(d)
                dl.pop(i)
                break

    sorted_rout.append(dl[0])

    return sorted_rout


def check_times(dl: list[dict]):
    rd = dict()
    for d in dl:
        if d['bus_id'] in rd:
            rd[d['bus_id']].append(d)
        else:
            rd[d['bus_id']] = [d]

    rd_rout_sorted = dict()
    for k,l in rd.items():
        rd_rout_sorted[k] = _sort_rout(l)

    error_d = dict()
    for k,l in rd_rout_sorted.items():
        for i in range(len(l)-1):
            t1 = time.fromisoformat(l[i]['a_time'])
            t2 = time.fromisoformat(l[i+1]['a_time'])
            if t1 < t2:
                pass
            else:
                error_d[k]=l[i+1]['stop_name']
                break


    print('Arrival time test:')
    if error_d:

        for k, v in error_d.items():
            print('bus_id line '+str(k)+': wrong time on station '+v)
    else:
        print('OK')


### part 6

def part6(dl):
    d_ = count_start_stop_and_name(dl)
    issue = []
    for d in dl:
        if d['stop_type'] == 'O':
            if d['stop_name'] in d_['trans']:
                issue.append(d['stop_name'])
    print('On demand stops test:')
    if issue:
        issue.sort()
        print('Wrong stop type: '+str(issue))
    else:
        print('OK')



if __name__ == '__main__':
    data_str = input()
    # print('data_str', data_str)
    data_dl = load_data(data_str)
    ## part 2
    # error_d = check_data(data_dl)
    # print_output(error_d)

    ##part3
    # stop_d = count_stops(data_dl)
    # print_stops(stop_d)

    ##part4
    # cont = check_start_stop(data_dl)
    # if cont:
    #     count_start_stop_and_name(data_dl)

    ## part 5
    # check_times(data_dl)

    ## part6
    part6(data_dl)

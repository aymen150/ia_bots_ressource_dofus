
import py.variable as v

class Map :
    def __init__(self, pos_cereale : list , pos : str , next_map : list )  :
        self.cereale = pos_cereale
        self.map = pos
        self.next_map = next_map
        
    

def circuit_amakna() -> list[Map] :    
        #6,6 V 6,7 > 7,7 V 7,8 V 7,9 > 8,9 >9,9 ^ 9,8 < 8,8 ^ 8,7 > 9,7 > 10,7 ^ 10,6 < 9,6 ^ 9,5 < 8,5 V 8,6 < ^ ^ 7,4> 8,4 < V V 6,6
    MAP = [Map(v.MAP_P6_P6,"6,6", [v.MAP_DOWN_M_T5]), 
       Map(v.MAP_P6_P7,"6,7", [v.MAP_RIGHT_M_T5]),
       Map(v.MAP_P7_P7,"7,7", [v.MAP_DOWN_M_T5]),
       Map( v.MAP_P7_P8,"7,8", [v.MAP_DOWN_M_T5 ] ),
       Map( v.MAP_P7_P9,"7,9", [v.MAP_RIGHT_M_T5 ] ),
       Map( v.MAP_P8_P9,"8,9", [v.MAP_RIGHT_M_T5 ] ),
       Map( v.MAP_P9_P9,"9,9", [v.MAP_TOP_M_T5 ] ),
       Map( v.MAP_P9_P8,"9,8", [v.MAP_LEFT_M_T5 ] ),
       Map( v.MAP_P8_P8,"8,8", [v.MAP_TOP_M_T5 ] ),
       Map( v.MAP_P8_P7,"8,7", [v.MAP_RIGHT_M_T8 ] ),
       Map( v.MAP_P9_P7,"9,7", [v.MAP_RIGHT_M_T8 ] ),
       Map( v.MAP_P10_P7,"10,7", [v.MAP_TOP_M_T8 ] ),
       Map( v.MAP_P10_P6,"10,6", [v.MAP_LEFT_M_T5 ] ),
       Map( v.MAP_P9_P6,"9,6", [v.MAP_TOP_M_T5 ] ),
       Map( v.MAP_P9_P5,"9,5", [v.MAP_LEFT_M_T5 ] ),
       Map( v.MAP_P8_P5,"8,5", [v.MAP_DOWN_M_T5 ] ),
       Map( v.MAP_P8_P6,"8,6", [v.MAP_LEFT_M_T8 ,v.MAP_TOP_M_T10, v.MAP_TOP_M_T10 ] ),
       Map( v.MAP_P7_P4,"7,4", [v.MAP_RIGHT_M_T5 ] ),
       Map( v.MAP_P8_P4,"8,4", [v.MAP_TOP_M_T5 ] )
    ]
    return MAP

def circuit_dragoeuf() :
    MAP =[ 
         Map([],"-1,24", v.map_m1_p24 ),
        Map([],"-2,24", v.map_m2_p24 ),
        Map([],"-3,24", v.map_m3_p24 ),
        Map([],"-4,24", v.map_m4_p24 ),
        Map([],"-5,24", v.map_m5_p24 ),
        Map([],"-5,25", v.map_m5_p25 ),
        Map([],"-6,25", v.map_m6_p25 ),
        Map([],"-6,26", v.map_m6_p26 ),
        Map([],"-6,27", v.map_m6_p27 ),
        Map([],"-7,27", v.map_m7_p27 ),
        Map([],"-7,28", v.map_m7_p28 ),
        Map([],"-7,29", v.map_m7_p29 ),
        Map([],"-7,30", v.map_m7_p30 ),
        Map([],"-7,31", v.map_m7_p31 ),
        Map([],"-7,32", v.map_m7_p32 ),
        Map([],"-6,32", v.map_m6_p32 ),
        Map([],"-5,32", v.map_m5_p32 ),
        Map([],"-4,32", v.map_m4_p32 ),
        Map([],"-3,32", v.map_m3_p32 ),
        Map([],"-3,31", v.map_m3_p31 ),
        Map([],"-4,31", v.map_m4_p31 ),
        Map([],"-5,31", v.map_m5_p31 ),
        Map([],"-6,31", v.map_m6_p31 ),
        Map([],"-6,30", v.map_m6_p30 ),
        Map([],"-5,30", v.map_m5_p30 ),
        Map([],"-4,30", v.map_m4_p30 ),
        Map([],"-3,30", v.map_m3_p30 ),
        Map([],"-2,30", v.map_m2_p30 ),
        Map([],"-1,30", v.map_m1_p30 ),
        Map([],"-1,29", v.map_m1_p29 ),
        Map([],"-2,29", v.map_m2_p29 ),
        Map([],"-3,29", v.map_m3_p29 ),
        Map([],"-4,29", v.map_m4_p29 ),
        Map([],"-5,29", v.map_m5_p29 ),
        Map([],"-6,29", v.map_m6_p29 ),
        Map([],"-6,28", v.map_m6_p28 ),
        Map([],"-5,28", v.map_m5_p28 ),
        Map([],"-4,28", v.map_m4_p28 ),
        Map([],"-3,28", v.map_m3_p28 ),
        Map([],"-2,28", v.map_m2_p28 ),
        Map([],"-1,28", v.map_m1_p28 ),
        Map([],"-2,27", v.map_m2_p27 ),
        Map([],"-3,27", v.map_m3_p27 ),
        Map([],"-4,27", v.map_m4_p27 ),
        Map([],"-5,27", v.map_m5_p27 ),
        Map([],"-5,26", v.map_m5_p26 ),
        Map([],"-4,26", v.map_m4_p26 ),
        Map([],"-3,26", v.map_m3_p26 ),
        Map([],"-2,26", v.map_m2_p26 ),
        Map([],"-1,26", v.map_m1_p26 ),
        Map([],"-1,25", v.map_m1_p25 )
        ]

    return MAP

def circuit_porco():
    MAP = [
        Map([],"-1,24", v.map_m1_p24  ),
        Map([],"0,24", v.map_p0_p24 ),
        Map([],"0,25", v.map_p0_p25 ),
        Map([],"0,26", v.map_p0_p26 ),
        Map([],"0,27", v.map_p0_p27 ),
        Map([],"0,28", v.map_p0_p28 ),
        Map([],"0,29", v.map_p0_p29 ),
        Map([],"0,30", v.map_p0_p30 ),
        Map([],"0,31", v.map_p0_p31_d ),
        Map([],"1,31", v.map_p1_p31 ),
        Map([],"1,32", v.map_p1_p32 ),
        Map([],"1,33", v.map_p1_p33 ),
        Map([],"1,34", v.map_p1_p34  ),
        Map([],"0,34", v.map_p0_p34  ),
        Map([],"-1,34", v.map_m1_p34  ),
        Map([],"-2,34", v.map_m2_p34  ),
        Map([],"-2,33", v.map_m2_p33 ),
        Map([],"-2,32", v.map_m2_p32  ),
        Map([],"-2,31", v.map_m2_p31  ),
        Map([],"-1,31", v.map_m1_p31 ),
        Map([],"-1,32", v.map_m1_p32 ),
        Map([],"-1,33", v.map_m1_p33  ),
        Map([],"0,33", v.map_p0_p33  ),
        Map([],"0,32", v.map_p0_p32  ),
        Map([],"0,31", v.map_p0_p31_h  )

    ]
    return MAP

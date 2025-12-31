% FARMERS(owner)
farmer(ana).
farmer(asdrubal).
farmer(miguel).
farmer(joao).
farmer(teresinha).
farmer(victor).
farmer(carlos).
farmer(anabela).

% FARMS(name, owner, region, type)
farm(q1, ana, alentejo, vinha).
farm(q2, ana, alentejo, olival).
farm(q3, asdrubal, lisboa, cenoureira).
farm(q4, asdrubal, lisboa, milharal).
farm(q5, asdrubal, lisboa, vinha).
farm(q6, miguel, evora, trigal).
farm(q7, miguel, evora, cenoureia).
farm(q8, miguel, evora, vinha).
farm(q9, miguel, evora, morangueira).
farm(q10, joao, porto, vinha).
farm(q11, joao, porto, trigal).
farm(q12, joao, porto, cenoureira).
farm(q13, teresinha, algarve, olival).
farm(q14, teresinha, algarve, vinha).
farm(q15, victor, setubal, olival).
farm(q16, victor, setubal, vinha).
farm(q17, victor, setubal, trigal).
farm(q18, carlos, sintra, milharal).
farm(q19, carlos, sintra, vinha).
farm(q20, anabela, coina, milharal).
farm(q21, anabela, coina, olival).
farm(q22, anabela, coina, trigal).

% SENSOR READINGS(name, type, value)
sensor_reading(q1,humidity,28).
sensor_reading(q2,humidity,35).
sensor_reading(q3,humidity,42).
sensor_reading(q4,humidity,38).
sensor_reading(q5,humidity,33).
sensor_reading(q6,humidity,45).
sensor_reading(q7,humidity,30).
sensor_reading(q8,humidity,36).
sensor_reading(q9,humidity,50).
sensor_reading(q10,humidity,41).
sensor_reading(q11,humidity,40).
sensor_reading(q12,humidity,44).
sensor_reading(q13,humidity,32).
sensor_reading(q14,humidity,29).
sensor_reading(q15,humidity,47).
sensor_reading(q16,humidity,39).
sensor_reading(q17,humidity,53).
sensor_reading(q18,humidity,27).
sensor_reading(q19,humidity,24).
sensor_reading(q20,humidity,31).
sensor_reading(q21,humidity,37).
sensor_reading(q22,humidity,46).
sensor_reading(q1, temperature, 25).
sensor_reading(q2, temperature, 25).
sensor_reading(q3, temperature, 25).
sensor_reading(q4, temperature, 25).
sensor_reading(q5, temperature, 25).
sensor_reading(q6, temperature, 25).
sensor_reading(q7, temperature, 25).
sensor_reading(q8, temperature, 25).
sensor_reading(q9, temperature, 25).
sensor_reading(q10, temperature, 25).
sensor_reading(q11, temperature, 25).
sensor_reading(q12, temperature, 25).
sensor_reading(q13, temperature, 25).
sensor_reading(q14, temperature, 25).
sensor_reading(q15, temperature, 25).
sensor_reading(q16, temperature, 25).
sensor_reading(q17, temperature, 25).
sensor_reading(q18, temperature, 25).
sensor_reading(q19, temperature, 25).
sensor_reading(q20, temperature, 25).
sensor_reading(q21, temperature, 25).
sensor_reading(q22, temperature, 25).
sensor_reading(q1, water, 47000).
sensor_reading(q2, water, 52500).
sensor_reading(q3, water, 39000).
sensor_reading(q5, water, 61000).
sensor_reading(q8, water, 58000).
sensor_reading(q10, water, 43000).
sensor_reading(q13, water, 72000).
sensor_reading(q16, water, 49000).
sensor_reading(q18, water, 35000).
sensor_reading(q21, water, 66500).
sensor_reading(q1, ph, 6.5).
sensor_reading(q2, ph, 4.7).
sensor_reading(q3, ph, 8.2).
sensor_reading(q4, ph, 7.0).
sensor_reading(q5, ph, 5.1).
sensor_reading(q6, ph, 8.0).
sensor_reading(q7, ph, 4.5).

% DISTRIBUTORS (name, region, capacity, demand level)
distributor(d1, alentejo, 1000, 2).
distributor(d2, lisboa, 800, 1).
distributor(d3, evora, 1200, 3).
distributor(d4, porto, 900, 2).
distributor(d5, algarve, 700, 2).
distributor(d6, setubal, 1100, 1).
distributor(d7, sintra, 950, 2).
distributor(d8, coina, 1000, 1).

% TRANSPORTS (name, capacity, type, autonomy, region, impact)
transport(t1, 1000, fossil, 100, alentejo, 3).
transport(t2, 500, electric, 10, alentejo, 1).
transport(t3, 800, fossil, 400, algarve, 5).
transport(t4, 700, hybrid, 300, setubal, 2).
transport(t5, 150, electric, 340, coina, 1).
transport(t6, 700, fossil, 220, porto, 3).
transport(t7, 900, hybrid, 350, evora, 2).
transport(t8, 1000, electric, 170, sintra, 1).

% Connections based on graph image

% Top of the network
link(q2, d1, 5).
link(q1, d1, 7).
link(q3, d1, 6).

% Network center
link(q3, q4, 8).
link(q4, d2, 6).
link(q4, d3, 7).
link(q4, q5, 5).
link(q4, d4, 6).

% Additional connections
link(q2, d2, 8).
link(q3, d3, 7).
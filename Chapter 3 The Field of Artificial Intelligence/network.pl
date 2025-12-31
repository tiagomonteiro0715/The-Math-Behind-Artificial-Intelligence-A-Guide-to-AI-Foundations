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
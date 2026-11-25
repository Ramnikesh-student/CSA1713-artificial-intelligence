

% Course eligibility rules

eligible(Name, Math, Programming, English) :-
    Math >= 60,
    Programming >= 60,
    English >= 50,
    write(Name),
    write(' is eligible for the course.').

eligible(Name, Math, Programming, English) :-
    (Math < 60;
     Programming < 60;
     English < 50),
    write(Name),
    write(' is not eligible for the course.').





% Fact
studies(kumar, ai).

% Rule 1
learns_intelligent_systems(X) :-
    studies(X, ai).

% Rule 2
solves_ai_problems(X) :-
    learns_intelligent_systems(X).




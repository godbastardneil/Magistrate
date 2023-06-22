consists(exam, quest1).
consists(exam, quest2).
consists(exam, quest3).
add_quest(Q):- assert(consists(exam, Q)).

consists(quest1, them1).
consists(quest1, them2).
consists(quest2, them3).
consists(quest3, them4).
add_them(Q, T):- assert(consists(Q, T)).

presence(them1).
presence(them2).
%presence(them3).
presence(them4).
find_them(T):- assert(presence(T)).

check(them1).
%check(them2).
%check(them3).
check(them4).
check_them(T):- presence(T), assert(check(T)).

%assert, retract

know(T):- presence(T), check(T).

clarity(Q):- consists(Q, T), know(T).
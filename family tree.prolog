
parent(john, jim).
parent(john, ann).
parent(mary, jim).
parent(mary, ann).
parent(jim, tom).
parent(jim, sue).
parent(ann, bob).

% Define the gender relationship
male(john).
male(jim).
male(tom).
male(bob).
female(mary).
female(ann).
female(sue).

% Define the sibling relationship
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Define the grandparent relationship
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

% Define the aunt/uncle relationship
aunt_or_uncle(X, Y) :-
    sibling(X, Z),
    parent(Z, Y).

% Define The Cousin Relationship
ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(Z, Y),
    ancestor(X, Z).

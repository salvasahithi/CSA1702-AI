symptom(feeling_feverish).
symptom(coughing).
symptom(headache).
symptom(body_aches).

condition(flu) :-
    symptom(feeling_feverish),
    symptom(coughing),
    symptom(headache),
    symptom(body_aches).

condition(cold) :-
    symptom(coughing),
    symptom(headache),
    symptom(body_aches).

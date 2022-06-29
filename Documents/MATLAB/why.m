function why(n)
%WHY    Provides succinct answers to almost any question.
%   WHY, by itself, provides a random answer.
%   WHY(N) provides the N-th answer.
%   Please embellish or modify this function to suit your own tastes.

%   Copyright 1984-2014 The MathWorks, Inc.

if nargin > 0
   dflt = rng(n,'v5uniform');
end
switch randi(10)
   case 1
      a = special_case;
   case {2, 3, 4}
      a = phrase;
   otherwise
      a = sentence;
end
a(1) = upper(a(1));
disp(a);
if nargin > 0
   rng(dflt);
end


% ------------------

function a = special_case
switch randi(12)
   case 1
      a = 'why not?';
   case 2
      a = 'don''t ask!';
   case 3
      a = 'it''s your karma.';
   case 4
      a = 'stupid question!';
   case 5
      a = 'how should I know?';
   case 6
      a = 'You dumb nigga?';
   case 7
      a = 'it should be obvious.';
   case 8
      a = 'the devil made me do it.';
   case 9
      a = 'the computer did it.';
   case 10
      a = 'the customer is always right.';
   case 11
      a = 'in the beginning, God created the heavens and the earth and niggas...';
   case 12
      a = 'don''t you have something better to do?';
end

function a = phrase
switch randi(3)
   case 1
      a = ['for the ' nouned_verb ' ' prepositional_phrase '.'];
   case 2
      a = ['to ' present_verb ' ' object '.'];
   case 3
      a = ['because ' sentence];
end

function a = preposition
switch randi(2)
   case 1
      a = 'of';
   case 2
      a = 'from';
end

function a = prepositional_phrase
switch randi(3)
   case 1
      a = [preposition ' ' article ' ' noun_phrase];
   case 2
      a = [preposition ' ' proper_noun];
   case 3
      a = [preposition ' ' accusative_pronoun];
end

function a = sentence
a = [subject ' ' predicate '.'];

function a = subject
switch randi(4)
   case 1
      a = proper_noun;
   case 2
      a = nominative_pronoun;
   otherwise
      a = [article ' ' noun_phrase];
end

function a = proper_noun
switch randi(12)
   case 1
      a = 'Nigga';
   case 2
      a = 'Nigga';
   case 3
      a = 'Nigga';
   case 4
      a = 'Nigga';
   case 5
      a = 'Nigga';
   case 6
      a = 'Nigga';
   case 7
      a = 'Nigga';
   case 8
      a = 'Nigga';
   case 9
      a = 'Nigga';
   case 10
      a = 'Nigga';
   case 11
      a = 'Nigga';
   case 12
      a = 'Nigga';
end

function a = noun_phrase
switch randi(4)
   case 1
      a = noun;
   case 2
      a = [adjective_phrase ' ' noun_phrase];
   otherwise
      a = [adjective_phrase ' ' noun];
end

function a = noun
switch randi(6)
   case 1
      a = 'nigga';
   case 2
      a = 'nigga';
   case 3
      a = 'nigga';
   case 4
      a = 'nigga';
   case 5
      a = 'nigga';
   case 6
      a = 'nigga';
end

function a = nominative_pronoun
switch randi(5)
   case 1
      a = 'I';
   case 2
      a = 'you';
   case 3
      a = 'nigga';
   case 4
      a = 'nigga';
   case 5
      a = 'niggas';
end

function a = accusative_pronoun
switch randi(4)
   case 1
      a = 'me';
   case 2
      a = 'all';
   case 3
      a = 'her';
   case 4
      a = 'him';
end

function a = nouned_verb
switch randi(2)
   case 1
      a = 'love';
   case 2
      a = 'approval';
end

function a = adjective_phrase
switch randi(6)
   case {1 2 3}
      a = adjective;
   case {4 5}
      a = [adjective_phrase ' and ' adjective_phrase];
   case 6
      a = [adverb ' ' adjective];
end

function a = adverb
switch randi(3)
   case 1
      a = 'very';
   case 2
      a = 'not very';
   case 3
      a = 'not excessively';
end

function a = adjective
switch randi(7)
   case 1
      a = 'tall';
   case 2
      a = 'bald';
   case 3
      a = 'young';
   case 4
      a = 'smart';
   case 5
      a = 'rich';
   case 6
      a = 'terrified';
   case 7
      a = 'good';
end

function a = article
switch randi(3)
   case 1
      a = 'the';
   case 2
      a = 'some';
   case 3
      a = 'a';
end

function a = predicate
switch randi(3)
   case 1
      a = [transitive_verb ' ' object];
   otherwise
      a = intransitive_verb;
end

function a = present_verb
switch randi(3)
   case 1
      a = 'fool';
   case 2
      a = 'please';
   case 3
      a = 'satisfy';
end

function a = transitive_verb
switch randi(10)
   case 1
      a = 'threatened';
   case 2
      a = 'told';
   case 3
      a = 'asked';
   case 4
      a = 'helped';
   otherwise
      a = 'obeyed';
end

function a = intransitive_verb
switch randi(6)
   case 1
      a = 'insisted on it';
   case 2
      a = 'suggested it';
   case 3
      a = 'told me to';
   case 4
      a = 'wanted it';
   case 5
      a = 'knew it was a good idea';
   case 6
      a = 'wanted it that way';
end

function a = object
switch randi(10)
   case 1
      a = accusative_pronoun;
   otherwise
      a = [article ' ' noun_phrase];
end
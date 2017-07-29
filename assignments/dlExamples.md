marriedTo(john1,margaret1)
Marriage(ma1)
spouseIn(john1,ma1)

spouseIn(margaret1,ma1)

yearOf(de1,1429)

Year(1429)
Event(1429)
deathOf(john1,de1)

Death(de1)

Person(john1)
Person(margaret1)

Event(ma1)

after(1429,1464)
during(1429,1429)


$\top \sqsubseteq \neg{\exists}marriedTo.Self$
$\top \sqsubseteq {\forall}marriedTo.Person
$Marriage \sqsubseteq Event$
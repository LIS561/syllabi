- ∀x(((Room(x) ∨ Corridor(x)) ∨ Stairwell(x)) → InternalArea(x))
- ∀x((((Balcony(x) ∨ ExitDischarge(x)) ∨ Court(x)) ∨ Yard(x)) → ExternalArea(x))
- ∀x((((Aisle(x) ∨ Stairway(x)) ∨ Passageway(x)) ∨ Ramp(x)) → Pathway(x))
- ∀x((Gateway(x) ∨ Doorway(x)) → Transition(x))
- ∀x((Gate(x) ∨ Door(x)) → Barrier(x))
- ∀x((InternalArea(x) ∨ ExternalArea(x)) → Area(x))
- ∀x((Pathway(x) ∨ Transition(x)) → Connection(x))
- ∀x∀y(Within(x,y) → (Area(x) ∧ Area(y)))
- ∀x∀y(To(x,y) → (Connection(x) ∧ Area(y)))
- ∀x∀y(Along(x,y) → (Transition(x) ∧ Pathway(y)))
- ∀x∀y(Seals(x,y) → (Barrier(x) ∧ Transition(y)))
- ∀x∀y(Includes(x,y) → (Area(x) ∧ Pathway(y)))

- ExitDischarge~D~ = X ⊆ E
- Ramp~D~ = R ⊆ E
- Pathway~D~ = P ⊆ E
- Transition~D~ = N ⊆ E
- Doorway~D~ = W ⊆ E
- To~D~ = T ⊆ C × A
- Along~D~ = L ⊆ N × P
- Includes~D~ = I ⊆ A × P
- Area~D~ = A ⊆ E
- Connection~D~ = C ⊆ E

- x ∈ X; ({x} × R) ∩ I  = ∅ 
- r ∈ R; (X × {r}) ∩ I  = ∅ 
- x ∈ X; r ∈ R; 〈x,r〉∈ I; ({x} × (R - {r})) ∩ I  = ∅; L ∩ (N × {r}) = ∅
- x ∈ X; r ∈ R; 〈x,r〉∈ I; ((X - x) × {r}) ∩ I  = ∅; L ∩ (N × {r}) = ∅
- x ∈ X; r ∈ R; 〈x,r〉∈ I; w ∈ W; 〈w,x〉∈ T; 〈w,r〉∉ L
- x ∈ X; r ∈ R; 〈x,r〉∈ I; w ∈ W; 〈w,x〉∈ T; 〈w,r〉∈ L
- None of the Above



~~~~
<v> ::= a|e|i|o|u|y
<c> ::= b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|z
<b> ::= <c>|<c><b>|<v><a>
<a> ::= <c><a>|<v><b>
~~~~

If <a> is the starting symbol, which of the following strings belong to
the language generated by this grammar?

1. alkalfhuirhfweuirhweirhus     (no)
2. aohffaoierhfierhgwirhwuireh   (no)
3. validhvauhuvihegeruishsuerg   (no)
4. aohuifgrefyyerfban            (yes)
5. aoauffsgfpbkpfbgo             (no)
6. gkfggk                        (no)
7. fjvviojsiv                    (yes) 
8. ijigghu                       (no)
9. oigrgregrgr                   (yes)
10. None of the above



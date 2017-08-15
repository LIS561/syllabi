The Harvard Personnel Manual section on domestic violence leave (http://hr.harvard.edu/staff-personnel-manual/time-away-work/domestic-violence-leave) defines the following categories of family members:

* Persons who are married to one another;
* Persons in a substantive dating or engagement relationship and who reside together;
* Persons having a child in common, regardless of whether they have ever married or resided together;
* A parent, step-parent, child, step-child, sibling, grandparent or grandchild;
* Persons in a guardianship relationship.
I propose to model the family relationships using these description logic axioms:

1. marriedTo ⊑ familyMember
2. marriedTo ≡ marriedTo⁻
3. dating ≡ dating⁻
4. engagedTo ≡ engagedTo⁻
5. residesWith ≡ residesWith⁻
6. datingOrEngaged ≡ dating ⊔ engagedTo
7. datingOrEngaged ⊓ residesWith ⊑ familyMember
8. parentOf ⊑ familyMember
9. parentOf ≡ childOf⁻
10. childOf ⊑ familyMember
11. parentOf ∘ childOf ⊑ familyMember
12. parentOf ∘ parentOf ⊑ familyMember
13. marriedTo ∘ parentOf ⊑ familyMember
14. childOf ∘ marriedTo ⊑ familyMember
15. childOf ∘ parentOf ⊑ familyMember
16. childOf ∘ childOf ⊑ familyMember
17. guardianOf ≡ hasGuardian⁻
18. guardianOf ⊔ hasGuardian ⊑ familyMember
I'd like to add the constraint that for purposes of these definitions, no one is a family member to himself or herself (e.g., sister to herself, her own parent, married to himself, etc.). My first thought is to add the following axiom as number 19:

⊤⊑ ¬∃familyMember.Self

a) But when I add that axiom, I find that no model will satisfy my combined A-Box, T-Box, and R-Box assertions. Why is that the case?

b) Using precise natural language (and description logic notation if useful) explain five specific inconsistencies that can arise from adding that last proposed axiom. Upload your answers here.  

c) It turns out that some A-Box configurations (such as an empty A-Box) admit interpretations that satisfy all 19 axioms. Describe a non-empty A-Box that would be consistent with all the axioms (including the problematic 19th).

d) Although I could add individual constraints that rule out being your own brother, spouse, parent, etc., I'd like to take care of all of them, either by modifying the proposed 19th, replacing it with an axiom that works better, or adding just a few additional axioms to solve the problem. Propose a simple solution that gives me those anti-reflexive constraints.

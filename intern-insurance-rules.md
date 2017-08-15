Look again at sections A-G of "Types of Employment" in the Harvard University Staff Employee Manual: http://hr.harvard.edu/staff-personnel-manual/requirements-conditions-employment/types-employment

I define the following predicates and constants:

Sx true if x is a student
Rx true if x is a recognized co-op or internship program.
Wwxyz true if w worked for program x during every week inclusive of weeks y and z.
Hwxyz true if w worked for program x for y hours during week z.
Ex true if x is eligible for health insurance coverage under the Affordable Care Act.
Gxy true if x is greater than or equal to y.
Mxyz true if x minus y is equal to z.
a is 8
b is 30
The section on co-op students and interns includes this sentence: "Co-op students and interns who work 30 hours a week or more for longer than 90 days will also be eligible for health insurance coverage under the Affordable Care Act."

My first attempt to model this rule using predicate logic is as follows:

 ∀v∀w∀x∃y∃z ((Sw ∧ (Rx ∧ (Wwxyz ∧ (Gzy ∧ (Mzyv ∧ (Gva ∧ ∀t∀u(Hwxtu ∧ Gtb))))))) → Ew)

Answer the following questions as best you can:

Paraphrase my attempt in English.
My rule does not capture every co-op student or intern who qualifies for health coverage per Harvard's rule. Explain at least one situation in which a student would qualify, but my rule would not include him or her. Try, if you can, to explain a second situation, different from the first, that my rule would also fail to capture.   
Would my attempt correctly classify any student employees as qualifying for health coverage? If yes, explain  the situation. If no, explain how you know the rule doesn't work at all.
Propose a modification to my rule (or a rule of your own) that correctly classifies as eligible for health coverage at least some students that my rule misses.
Choose any other rule on this page that you wish, and propose a translation of it into predicate logic.
Write paragraph of comments and reflections on challenges for analyzing these policies.

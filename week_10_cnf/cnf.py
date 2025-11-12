function CNF(formula)
    formula ← eliminate_implications(formula)
    formula ← move_negations_inward(formula)
    formula ← distribute_or_over_and(formula)
    formula ← simplify(formula)
    return formula
end function


function eliminate_implications(f)
    replace (A → B) with (¬A ∨ B)
    replace (A ↔ B) with ((A ∧ B) ∨ (¬A ∧ ¬B))
    return f
end function


function move_negations_inward(f)
    replace ¬(A ∧ B) with (¬A ∨ ¬B)
    replace ¬(A ∨ B) with (¬A ∧ ¬B)
    replace ¬(¬A) with A
    return f
end function


function distribute_or_over_and(f)
    repeat
        replace (A ∨ (B ∧ C)) with ((A ∨ B) ∧ (A ∨ C))
        replace ((A ∧ B) ∨ C) with ((A ∨ C) ∧ (B ∨ C))
    until no changes
    return f
end function

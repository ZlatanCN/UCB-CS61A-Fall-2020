(define (split-at lst n)
    'YOUR-CODE-HERE
    (define (length lst)
        (if (null? lst)
            0
            (+ 1 (length (cdr lst)))
        )
    )
    (cond
        ((= n 0) (cons nil lst))
        ((> n (length lst)) (cons lst nil))
        (else (cons (cons (car lst) (car (split-at (cdr lst) (- n 1)))) (cdr (split-at (cdr lst) (- n 1)))))
    )
)


(define (compose-all funcs)
    'YOUR-CODE-HERE
    (define (helper x)
        (if (null? funcs)
            x
            ((compose-all (cdr funcs)) ((car funcs) x))
        )
    )
    helper
)


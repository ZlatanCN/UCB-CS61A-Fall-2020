(define (factorial x)
    (cond 
          ((< x 0) 'Error)
          ((= x 0) 1)
          ((= x 1) 1)
          (else (* x (factorial (- x 1))))
    )
)


(define (fib n)
    (cond 
          ((= n 0) 0)
          ((= n 1) 1)
          (else (+ (fib (- n 1)) (fib (- n 2))))
    )
)


(define (my-append a b)
    (cond 
          ((null? a) b)
          ((null? b) a)
          (else (cons (car a) (my-append (cdr a) b)))
    )
)


(define (duplicate lst)
    (if (null? lst) 
        '() 
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)


(define (insert element lst index)
    (cond 
          ((and (null? lst) (not (= index 0))) '())
          ((< index 0) lst)
          ((= index 0) (cons element lst))
          (else (cons (car lst) (insert element (cdr lst) (- index 1))))
    )
)
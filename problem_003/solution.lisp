(defun find-largest-prime-in (number)
  (do ((n 2 (1+ n))
       (prime 2))
      ((= 1 number) prime)
    (when (= 0 (mod number n))
      (setf prime n)
      (loop
	 (when (/= 0 (mod number n))
	   (return))
	 (setf number (/ number n))))))

(find-largest-prime-in 600851475143)

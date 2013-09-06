(defun sum-numbers-mod-3-5 ()
  (do ((n 0 (1+ n))
       (sum 0))
      ((= 1000 n) sum)
    (if (or (= 0 (mod n 3)) (= 0 (mod n 5)))
      (incf sum n))))

(sum-numbers-mod-3-5)

(provide 'some-23-solution)
(defun find-evenly-divisible-number ()
    (let ((n 2520))
      (loop
	 (when (and (= 0 (mod n 20)) 
		    (= 0 (mod n 19)) 
		    (= 0 (mod n 18)) 
		    (= 0 (mod n 17)) 
		    (= 0 (mod n 16)) 
		    (= 0 (mod n 15)) 
		    (= 0 (mod n 14))
		    (= 0 (mod n 13))
		    (= 0 (mod n 12)) 
		    (= 0 (mod n 11)))
	   (return n))
	 (incf n 2520))))
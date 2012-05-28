(require 'cl)

(defun find-largest-product()
  (do ((start 1 (1+ start))
       (end 6 (1+ end))
       (product 0))
      ((= end 1001) product)
    (with-temp-buffer
       (insert-file-contents "./1000digitNumber.txt")
       (do ((tmpproduct 1)
            (tmppos start (1+ tmppos)))
           ((= tmppos end) (if (> tmpproduct product) (setq product tmpproduct)))
         (let ((tmpnumber (string-to-number (buffer-substring tmppos (+ 1 tmppos)))))
           (setq tmpproduct (* tmpproduct tmpnumber)))))))

(find-largest-product)

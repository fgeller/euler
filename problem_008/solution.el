(require 'cl)

(defun find-largest-product()
  (with-temp-buffer
    (insert-file-contents "./1000digitNumber.txt")
    (do ((start 1 (1+ start))
         (end 6 (1+ end))
         (product 0))
        ((= end 1001) product)
      (do ((tmp-product 1)
           (tmp-pos start (1+ tmp-pos)))
          ((= tmp-pos end) (if (> tmp-product product) (setq product tmp-product)))
        (let ((tmp-number (string-to-number (buffer-substring tmp-pos (+ 1 tmp-pos)))))
          (setq tmp-product (* tmp-product tmp-number)))))))

(find-largest-product)

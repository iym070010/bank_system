

CREATE DATABASE IF NOT EXISTS dbtest DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE dbtest;



/***************************************************************************
1：创建还款表payment表及插入数据 payment( loan_number,  payment_number, payment_datetime, payment_amount ) 
*******************************************************************************/

CREATE TABLE payment(
	loan_number CHAR(10),	##借款号
	payment_number CHAR(10),	##还款号
	payment_amount INT,
	payment_datetime DATETIME NOT NULL,	##插入记录的时间
	PRIMARY KEY (loan_number,payment_number)
);



SELECT * FROM payment;

drop table payment;

/***************************************************************************
2：创建贷款表loan表及插入数据 
*******************************************************************************/

CREATE TABLE loan(
	loan_number CHAR(10),	#-借款号
	branch_number CHAR(10),	#-支行号
	amount INT,
	PRIMARY KEY (loan_number)
);

drop table loan ;
#-----------------插入数据------------------

INSERT INTO loan VALUES ('000000001','Cbank','55555');
INSERT INTO loan VALUES ('000000021','Cbank','44444');
INSERT INTO loan VALUES ('000000301','Cbank','90110');
INSERT INTO loan VALUES ('000002401','Cbank','8888');
INSERT INTO loan VALUES ('000032001','Cbank','99999');
INSERT INTO loan VALUES ('000010001','Cbank','11111');
INSERT INTO loan VALUES ('000210001','Cbank','10000');
INSERT INTO loan VALUES ('000030541','Cbank','212');



ALTER TABLE loan ADD PayOverDate DATETIME;	#-添加一列PayOverDate用于记录还款完成日期

SELECT * FROM loan;
#---------------------------------------------


/****************************
一、创建 转账存储过程
*****************************/
DROP PROCEDURE IF EXISTS HuanQian_02;	#存在则删除存储过程
												#-为了DROP这个存储过程
####

#mysql存储过程：还款
#
DELIMITER //
  CREATE PROCEDURE HuanQian_02(IN payment_no_x CHAR(10),loan_no_y CHAR(10),payment_k INT,OUT error_num INT,OUT remain_payment INT)
    label:BEGIN
		DECLARE Paymentamount INT;
		IF (SELECT amount 			 
			FROM loan
			WHERE loan_number = loan_no_y) IS NULL THEN
			SET error_num=-1;
            SET remain_payment=-1;
            LEAVE label;
		END IF;
        #修改payment表
		IF	(SELECT payment_amount 			#不存在借款账户
			 FROM payment
			 WHERE payment_number = payment_no_x) IS NULL THEN
			INSERT INTO payment values (loan_no_y,payment_no_x,payment_k,SYSDATE());
		ELSE 
			UPDATE payment
			SET payment_amount=payment_amount+payment_k
			WHERE payment_number=payment_no_x;
		END IF;
        
        #mysql的异常处理机制
 #       DECLARE exit HANDLER FOR SQLSTATE '23000' ,SQLSTATE '42000',SQLSTATE ''
 #       SET ;
        
        #修改loan表
		SELECT payment_amount into Paymentamount#这里出现错误
		FROM payment
		WHERE payment_number=payment_no_x;
        
		SELECT amount-Paymentamount into remain_payment
		FROM loan
		WHERE loan_number=loan_no_y;
        
        SELECT Paymentamount,remain_payment;#检查
        
		IF remain_payment<=0 THEN
			UPDATE loan
			SET PayOverDate = SYSDATE()
			WHERE loan_number=loan_no_y ;
		END IF;
        SET error_num=0;
		SELECT Paymentamount,remain_payment,error_num;#检查
    END label;
    //
DELIMITER ;

#调用：
SET SQL_SAFE_UPDATES = 0;	#设置批量更新数据
CALL HuanQian_02('1234567891','000000001',53355,@A,@B);
SELECT @A,@B;
SELECT * FROM payment;
SELECT * FROM loan;

use dbtest;
SELECT * FROM account;

update account set balance=balance+100 WHERE account_number='A-101';
	
insert into loan(loan_number,branch_number,amount,PayOverDate) values('123456','Cbank','1000',DBNull.Value);



SELECT * FROM loan;
SELECT * FROM payment;
SELECT * FROM account;









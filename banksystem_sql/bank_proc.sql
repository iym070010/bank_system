
USE dbtest;


CREATE TABLE account(
	account_number CHAR(10),	#--账号
	balance INT CHECK (balance >= 0),#	--账户余额
    Create_time DATETIME NOT NULL,
	PRIMARY KEY (account_number)
);

INSERT INTO account VALUES ('A-101','505',SYSDATE());
INSERT INTO account VALUES ('A-102','400',SYSDATE());
INSERT INTO account VALUES ('A-201','900',SYSDATE());
INSERT INTO account VALUES ('A-215','700',SYSDATE());
INSERT INTO account VALUES ('A-217','750',SYSDATE());
INSERT INTO account VALUES ('A-222','700',SYSDATE());
INSERT INTO account VALUES ('A-305','350',SYSDATE());
INSERT INTO account VALUES ('A-213','250',SYSDATE());
INSERT INTO account VALUES ('A-214','0',SYSDATE());

SELECT * FROM account;

/****************************
一、创建 转账存储过程
*****************************/
#-说明: account表中的 balance属性必须有>=0约束。否则，转账仍可完成，但结果balance会出现负数。

#-删除同名存储过程，方便开发中调试存储过程程序
DROP PROCEDURE IF EXISTS PTransfer;	

DELIMITER //
  CREATE PROCEDURE PTransfer(IN account_no_x CHAR(10),account_no_y CHAR(10),amount_k INT,OUT ErrorVar INT)
    label:BEGIN
		IF  (SELECT balance 
			 FROM account 
			 WHERE account_number = account_no_x) IS NULL 
			OR
			(SELECT balance 
			 FROM account 
			 WHERE account_number = account_no_y) IS NULL THEN
			SET ErrorVar=-1;
			LEAVE label;
		END IF;
		#######
		UPDATE account	
		SET balance = balance + amount_k
		WHERE account_number = account_no_y;
		#-（1）**********X账号减去k元***********
		UPDATE account
		SET balance = balance - amount_k
		WHERE account_number = account_no_x;
        
        SET ErrorVar=0; 
		COMMIT;
        
	END label;
    //
DELIMITER ;

#调用：
SELECT * FROM account;
SET SQL_SAFE_UPDATES = 0;	#设置批量更新数据
CALL PTransfer('A-101','A-102',100,@A);
SELECT @A;
SELECT * FROM account;

EXECUTE @retstat = PTransfer 'A-101', 'A-201', 100
SELECT @retstat	--显示存储过程执行的返回值，用于调试程序，可注释掉
IF @retstat = 0
	SELECT '转账成功。'
ELSE 
	SELECT '转账失败！'
--注释：主调程序（可以是其它高级语言）获取存储过程的出错代码，可据此查找具体的出错原因。
	
--3）对比转账前数据，观察数据是否正确


--2. *******转账失败(违反“余额大于0”约束)，事务回滚，数据库仍保持一致性*******
--可多次执行转账调用或修改转账金额，使存储过程违反约束，以测试程序的执行状态。


--<完>


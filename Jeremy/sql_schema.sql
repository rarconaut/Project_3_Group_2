DROP TABLE train_balanced;

CREATE TABLE train_balanced (
	enrollee_id VARCHAR(100),
	city VARCHAR(100),
	gender VARCHAR(100),
	relevent_experience VARCHAR(100),
	enrolled_university VARCHAR(100),
	education_level VARCHAR(100),
	major_discipline VARCHAR(100),
	experience VARCHAR(100),
	company_size VARCHAR(100),
	company_type VARCHAR(100),
	target INT
);

SELECT * FROM train_balanced;



DROP TABLE test_balanced;

CREATE TABLE test_balanced (
	enrollee_id VARCHAR(100),
	city VARCHAR(100),
	gender VARCHAR(100),
	relevent_experience VARCHAR(100),
	enrolled_university VARCHAR(100),
	education_level VARCHAR(100),
	major_discipline VARCHAR(100),
	experience VARCHAR(100),
	company_size VARCHAR(100),
	company_type VARCHAR(100),
	target INT
);

SELECT * FROM test_balanced;

SELECT * FROM response;
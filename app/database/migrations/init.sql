CREATE TABLE prior_authorizations (
    id SERIAL PRIMARY KEY,
    patient_name VARCHAR(255),
    insurance_id VARCHAR(255),
    status VARCHAR(100)
);
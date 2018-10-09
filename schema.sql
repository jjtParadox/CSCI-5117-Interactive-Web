drop table results;

create table results(
    result_id SERIAL PRIMARY KEY,
    name varchar(255) not null,
    participation varchar(5),
    last_participated varchar(10),
    participation_info text,
    learn_more varchar(5)
);
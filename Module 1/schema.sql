drop table results;

create table results(
    result_id SERIAL PRIMARY KEY,
    result_time timestamp not null default now(),
    name varchar(255) not null,
    participation varchar(5),
    last_participated varchar(10),
    participation_info text,
    learn_more bool
);
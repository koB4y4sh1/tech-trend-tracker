create table articles (
    id serial primary key,
    title text,
    summary text,
    url text,
    published timestamp
);

create table repos (
    id serial primary key,
    owner text,
    repo text,
    stars integer
);

create table stars (
    id serial primary key,
    repo_id integer references repos(id),
    date timestamp,
    star_count integer
);
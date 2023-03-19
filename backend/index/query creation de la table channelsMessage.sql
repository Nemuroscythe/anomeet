CREATE TABLE IF NOT EXISTS public."channelsMessage"
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    author uuid NOT NULL,
    date date NOT NULL DEFAULT now(),
    channel smallint NOT NULL DEFAULT 1,
    content text,
    PRIMARY KEY (id)
);

ALTER TABLE public."channelsMessage"
    OWNER to "test-anomeet_application";

COMMENT ON TABLE public."channelsMessage"
    IS 'Table contenant les messages liés à la page principales';
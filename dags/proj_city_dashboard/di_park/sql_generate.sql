DROP TABLE IF EXISTS public.di_park;
DROP TRIGGER IF EXISTS di_park_mtime ON public.di_park;
DROP SEQUENCE IF EXISTS public.di_park_ogc_fid_seq;
    
    -- create sequnce
    CREATE SEQUENCE IF NOT EXISTS public.di_park_ogc_fid_seq
        INCREMENT 1
        START 1
        MINVALUE 1
        MAXVALUE 9223372036854775807
        CACHE 1;
    
    
    -- grant sequnce
    ALTER TABLE IF EXISTS public.di_park_ogc_fid_seq OWNER to postgres;
    GRANT ALL ON TABLE public.di_park_ogc_fid_seq TO postgres WITH GRANT OPTION;
    
    -- create table
    CREATE TABLE IF NOT EXISTS public.di_park
    (
                seqno int,
        pm_name text,
        pm_longitude numeric,
        pm_latitude numeric,
        pm_unit text,
        pm_location text,
        di_hospital text,
        di_fire text,
        di_police text,
        capacity int
            ,
        ogc_fid integer NOT NULL DEFAULT nextval('di_park_ogc_fid_seq'::regclass),
            
        CONSTRAINT di_park_pkey PRIMARY KEY (ogc_fid)
        
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    
    -- grant table
    ALTER TABLE IF EXISTS public.di_park OWNER to postgres;
    GRANT ALL ON TABLE public.di_park TO postgres WITH GRANT OPTION;
    
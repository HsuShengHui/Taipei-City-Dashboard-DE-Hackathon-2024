DROP TABLE IF EXISTS public.toilet;
DROP TRIGGER IF EXISTS toilet_mtime ON public.toilet;
DROP SEQUENCE IF EXISTS public.toilet_ogc_fid_seq;
    
    -- create sequnce
    CREATE SEQUENCE IF NOT EXISTS public.toilet_ogc_fid_seq
        INCREMENT 1
        START 1
        MINVALUE 1
        MAXVALUE 9223372036854775807
        CACHE 1;
    
    
    -- grant sequnce
    ALTER TABLE IF EXISTS public.toilet_ogc_fid_seq OWNER to postgres;
    GRANT ALL ON TABLE public.toilet_ogc_fid_seq TO postgres WITH GRANT OPTION;
    
    -- create table
    CREATE TABLE IF NOT EXISTS public.toilet
    (
                data_time timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        district character varying(50) COLLATE pg_catalog."default",
        toilet_type character varying(50) COLLATE pg_catalog."default",
        toilet_name character varying(255) COLLATE pg_catalog."default",
        toilet_address text COLLATE pg_catalog."default",
        lng double precision,
        lat double precision,
        wkb_geometry geometry(Point,4326),
        management_unit character varying(255) COLLATE pg_catalog."default",
        seats integer,
        excellent integer,
        superior integer,
        normal integer,
        improved integer,
        accessible_seats integer,
        family_seats integer,
        _ctime timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        _mtime timestamp with time zone DEFAULT CURRENT_TIMESTAMP
            ,
        ogc_fid integer NOT NULL DEFAULT nextval('toilet_ogc_fid_seq'::regclass),
            
        CONSTRAINT toilet_pkey PRIMARY KEY (ogc_fid)
        
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    
    -- grant table
    ALTER TABLE IF EXISTS public.toilet OWNER to postgres;
    GRANT ALL ON TABLE public.toilet TO postgres WITH GRANT OPTION;
    
    
    -- create mtime trigger
    CREATE TRIGGER toilet_mtime
        BEFORE INSERT OR UPDATE 
        ON public.toilet
        FOR EACH ROW
        EXECUTE PROCEDURE public.trigger_set_timestamp();
    DROP TABLE IF EXISTS public.toilet_history;
DROP TRIGGER IF EXISTS toilet_history_mtime ON public.toilet_history;
DROP SEQUENCE IF EXISTS public.toilet_history_ogc_fid_seq;
    
    -- create sequnce
    CREATE SEQUENCE IF NOT EXISTS public.toilet_history_ogc_fid_seq
        INCREMENT 1
        START 1
        MINVALUE 1
        MAXVALUE 9223372036854775807
        CACHE 1;
    
    
    -- grant sequnce
    ALTER TABLE IF EXISTS public.toilet_history_ogc_fid_seq OWNER to postgres;
    GRANT ALL ON TABLE public.toilet_history_ogc_fid_seq TO postgres WITH GRANT OPTION;
    
    -- create table
    CREATE TABLE IF NOT EXISTS public.toilet_history
    (
                data_time timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        district character varying(50) COLLATE pg_catalog."default",
        toilet_type character varying(50) COLLATE pg_catalog."default",
        toilet_name character varying(255) COLLATE pg_catalog."default",
        toilet_address text COLLATE pg_catalog."default",
        lng double precision,
        lat double precision,
        wkb_geometry geometry(Point,4326),
        management_unit character varying(255) COLLATE pg_catalog."default",
        seats integer,
        excellent integer,
        superior integer,
        normal integer,
        improved integer,
        accessible_seats integer,
        family_seats integer,
        _ctime timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        _mtime timestamp with time zone DEFAULT CURRENT_TIMESTAMP
            ,
        ogc_fid integer NOT NULL DEFAULT nextval('toilet_history_ogc_fid_seq'::regclass),
            
        CONSTRAINT toilet_history_pkey PRIMARY KEY (ogc_fid)
        
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    
    -- grant table
    ALTER TABLE IF EXISTS public.toilet_history OWNER to postgres;
    GRANT ALL ON TABLE public.toilet_history TO postgres WITH GRANT OPTION;
    
    
    -- create mtime trigger
    CREATE TRIGGER toilet_history_mtime
        BEFORE INSERT OR UPDATE 
        ON public.toilet_history
        FOR EACH ROW
        EXECUTE PROCEDURE public.trigger_set_timestamp();
    
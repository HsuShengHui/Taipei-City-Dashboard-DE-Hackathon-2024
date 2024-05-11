DROP TABLE IF EXISTS public.medicine;
DROP TRIGGER IF EXISTS medicine_mtime ON public.medicine;
DROP SEQUENCE IF EXISTS public.medicine_ogc_fid_seq;
    
    -- create sequnce
    CREATE SEQUENCE IF NOT EXISTS public.medicine_ogc_fid_seq
        INCREMENT 1
        START 1
        MINVALUE 1
        MAXVALUE 9223372036854775807
        CACHE 1;
    
    
    -- grant sequnce
    ALTER TABLE IF EXISTS public.medicine_ogc_fid_seq OWNER to postgres;
    GRANT ALL ON TABLE public.medicine_ogc_fid_seq TO postgres WITH GRANT OPTION;
    
    -- create table
    CREATE TABLE IF NOT EXISTS public.medicine
    (
                data_time timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        name character varying(50) COLLATE pg_catalog."default",
        district character varying(50) COLLATE pg_catalog."default",
        addr character varying(50) COLLATE pg_catalog."default",
        phone character varying(50) COLLATE pg_catalog."default",
        lng double precision,
        lat double precision,
        wkb_geometry geometry(Point,4326),
        _ctime timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        _mtime timestamp with time zone DEFAULT CURRENT_TIMESTAMP
            ,
        ogc_fid integer NOT NULL DEFAULT nextval('medicine_ogc_fid_seq'::regclass),
            
        CONSTRAINT medicine_pkey PRIMARY KEY (ogc_fid)
        
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    
    -- grant table
    ALTER TABLE IF EXISTS public.medicine OWNER to postgres;
    GRANT ALL ON TABLE public.medicine TO postgres WITH GRANT OPTION;
    
    
    -- create mtime trigger
    CREATE TRIGGER medicine_mtime
        BEFORE INSERT OR UPDATE 
        ON public.medicine
        FOR EACH ROW
        EXECUTE PROCEDURE public.trigger_set_timestamp();
    DROP TABLE IF EXISTS public.medicine_history;
DROP TRIGGER IF EXISTS medicine_history_mtime ON public.medicine_history;
DROP SEQUENCE IF EXISTS public.medicine_history_ogc_fid_seq;
    
    -- create sequnce
    CREATE SEQUENCE IF NOT EXISTS public.medicine_history_ogc_fid_seq
        INCREMENT 1
        START 1
        MINVALUE 1
        MAXVALUE 9223372036854775807
        CACHE 1;
    
    
    -- grant sequnce
    ALTER TABLE IF EXISTS public.medicine_history_ogc_fid_seq OWNER to postgres;
    GRANT ALL ON TABLE public.medicine_history_ogc_fid_seq TO postgres WITH GRANT OPTION;
    
    -- create table
    CREATE TABLE IF NOT EXISTS public.medicine_history
    (
                data_time timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        name character varying(50) COLLATE pg_catalog."default",
        district character varying(50) COLLATE pg_catalog."default",
        addr character varying(50) COLLATE pg_catalog."default",
        phone character varying(50) COLLATE pg_catalog."default",
        lng double precision,
        lat double precision,
        wkb_geometry geometry(Point,4326),
        _ctime timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        _mtime timestamp with time zone DEFAULT CURRENT_TIMESTAMP
            ,
        ogc_fid integer NOT NULL DEFAULT nextval('medicine_history_ogc_fid_seq'::regclass),
            
        CONSTRAINT medicine_history_pkey PRIMARY KEY (ogc_fid)
        
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    
    -- grant table
    ALTER TABLE IF EXISTS public.medicine_history OWNER to postgres;
    GRANT ALL ON TABLE public.medicine_history TO postgres WITH GRANT OPTION;
    
    
    -- create mtime trigger
    CREATE TRIGGER medicine_history_mtime
        BEFORE INSERT OR UPDATE 
        ON public.medicine_history
        FOR EACH ROW
        EXECUTE PROCEDURE public.trigger_set_timestamp();
    
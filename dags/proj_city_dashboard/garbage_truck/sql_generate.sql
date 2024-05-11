DROP TABLE IF EXISTS public.garbage_truck;
DROP TRIGGER IF EXISTS garbage_truck_mtime ON public.garbage_truck;
DROP SEQUENCE IF EXISTS public.garbage_truck_ogc_fid_seq;
    
    -- create sequnce
    CREATE SEQUENCE IF NOT EXISTS public.garbage_truck_ogc_fid_seq
        INCREMENT 1
        START 1
        MINVALUE 1
        MAXVALUE 9223372036854775807
        CACHE 1;
    
    
    -- grant sequnce
    ALTER TABLE IF EXISTS public.garbage_truck_ogc_fid_seq OWNER to postgres;
    GRANT ALL ON TABLE public.garbage_truck_ogc_fid_seq TO postgres WITH GRANT OPTION;
    
    -- create table
    CREATE TABLE IF NOT EXISTS public.garbage_truck
    (
                district character varying(50) COLLATE pg_catalog."default",
        village character varying(50) COLLATE pg_catalog."default",
        team character varying(50) COLLATE pg_catalog."default",
        station character varying(50) COLLATE pg_catalog."default",
        car_number character varying(50) COLLATE pg_catalog."default",
        route character varying(50) COLLATE pg_catalog."default",
        arrival_time timestamp without time zone,
        departure_time timestamp without time zone,
        location text COLLATE pg_catalog."default",
        lng double precision,
        lat double precision,
        _ctime timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        _mtime timestamp with time zone DEFAULT CURRENT_TIMESTAMP
            ,
        ogc_fid integer NOT NULL DEFAULT nextval('garbage_truck_ogc_fid_seq'::regclass),
            
        CONSTRAINT garbage_truck_pkey PRIMARY KEY (ogc_fid)
        
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    
    -- grant table
    ALTER TABLE IF EXISTS public.garbage_truck OWNER to postgres;
    GRANT ALL ON TABLE public.garbage_truck TO postgres WITH GRANT OPTION;
    
    
    -- create mtime trigger
    CREATE TRIGGER garbage_truck_mtime
        BEFORE INSERT OR UPDATE 
        ON public.garbage_truck
        FOR EACH ROW
        EXECUTE PROCEDURE public.trigger_set_timestamp();
    DROP TABLE IF EXISTS public.garbage_truck_history;
DROP TRIGGER IF EXISTS garbage_truck_history_mtime ON public.garbage_truck_history;
DROP SEQUENCE IF EXISTS public.garbage_truck_history_ogc_fid_seq;
    
    -- create sequnce
    CREATE SEQUENCE IF NOT EXISTS public.garbage_truck_history_ogc_fid_seq
        INCREMENT 1
        START 1
        MINVALUE 1
        MAXVALUE 9223372036854775807
        CACHE 1;
    
    
    -- grant sequnce
    ALTER TABLE IF EXISTS public.garbage_truck_history_ogc_fid_seq OWNER to postgres;
    GRANT ALL ON TABLE public.garbage_truck_history_ogc_fid_seq TO postgres WITH GRANT OPTION;
    
    -- create table
    CREATE TABLE IF NOT EXISTS public.garbage_truck_history
    (
                district character varying(50) COLLATE pg_catalog."default",
        village character varying(50) COLLATE pg_catalog."default",
        team character varying(50) COLLATE pg_catalog."default",
        station character varying(50) COLLATE pg_catalog."default",
        car_number character varying(50) COLLATE pg_catalog."default",
        route character varying(50) COLLATE pg_catalog."default",
        arrival_time timestamp without time zone,
        departure_time timestamp without time zone,
        location text COLLATE pg_catalog."default",
        lng double precision,
        lat double precision,
        _ctime timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        _mtime timestamp with time zone DEFAULT CURRENT_TIMESTAMP
            ,
        ogc_fid integer NOT NULL DEFAULT nextval('garbage_truck_history_ogc_fid_seq'::regclass),
            
        CONSTRAINT garbage_truck_history_pkey PRIMARY KEY (ogc_fid)
        
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    
    -- grant table
    ALTER TABLE IF EXISTS public.garbage_truck_history OWNER to postgres;
    GRANT ALL ON TABLE public.garbage_truck_history TO postgres WITH GRANT OPTION;
    
    
    -- create mtime trigger
    CREATE TRIGGER garbage_truck_history_mtime
        BEFORE INSERT OR UPDATE 
        ON public.garbage_truck_history
        FOR EACH ROW
        EXECUTE PROCEDURE public.trigger_set_timestamp();
    
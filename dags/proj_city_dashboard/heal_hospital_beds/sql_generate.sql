DROP TABLE IF EXISTS public.heal_hospital_beds;
DROP TRIGGER IF EXISTS heal_hospital_beds_mtime ON public.heal_hospital_beds;
DROP SEQUENCE IF EXISTS public.heal_hospital_beds_ogc_fid_seq;
    
    -- create sequnce
    CREATE SEQUENCE IF NOT EXISTS public.heal_hospital_beds_ogc_fid_seq
        INCREMENT 1
        START 1
        MINVALUE 1
        MAXVALUE 9223372036854775807
        CACHE 1;
    
    
    -- grant sequnce
    ALTER TABLE IF EXISTS public.heal_hospital_beds_ogc_fid_seq OWNER to postgres;
    GRANT ALL ON TABLE public.heal_hospital_beds_ogc_fid_seq TO postgres WITH GRANT OPTION;
    
    -- create table
    CREATE TABLE IF NOT EXISTS public.heal_hospital_beds
    (
                data_time timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        name character varying(50) COLLATE pg_catalog."default",
        district character varying(50) COLLATE pg_catalog."default",
        addr character varying(50) COLLATE pg_catalog."default",
        phone character varying(50) COLLATE pg_catalog."default",
        acute_general_beds integer,
        acute_psychiatric_beds integer,
        chronic_general_beds integer,
        chronic_psychiatric_beds integer,
        palliative_beds integer,
        icu_beds integer,
        acute_respiratory_care_beds integer,
        chronic_respiratory_care_beds integer,
        burn_beds integer,
        emergency_observation_beds integer,
        other_observation_beds integer,
        surgical_recovery_beds integer,
        baby_beds integer,
        baby_sick_beds integer,
        hemodialysis_beds integer,
        peritoneal_dialysis_beds integer,
        psychiatric_icu_beds integer,
        burn_icu_beds integer,
        general_isolation_beds integer,
        positive_pressure_isolation_beds integer,
        negative_pressure_isolation_beds integer,
        bone_marrow_transplant_beds integer,
        lng double precision,
        lat double precision,
        wkb_geometry geometry(Point,4326),
        _ctime timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        _mtime timestamp with time zone DEFAULT CURRENT_TIMESTAMP
            ,
        ogc_fid integer NOT NULL DEFAULT nextval('heal_hospital_beds_ogc_fid_seq'::regclass),
            
        CONSTRAINT heal_hospital_beds_pkey PRIMARY KEY (ogc_fid)
        
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    
    -- grant table
    ALTER TABLE IF EXISTS public.heal_hospital_beds OWNER to postgres;
    GRANT ALL ON TABLE public.heal_hospital_beds TO postgres WITH GRANT OPTION;
    
    
    -- create mtime trigger
    CREATE TRIGGER heal_hospital_beds_mtime
        BEFORE INSERT OR UPDATE 
        ON public.heal_hospital_beds
        FOR EACH ROW
        EXECUTE PROCEDURE public.trigger_set_timestamp();
    DROP TABLE IF EXISTS public.heal_hospital_beds_history;
DROP TRIGGER IF EXISTS heal_hospital_beds_history_mtime ON public.heal_hospital_beds_history;
DROP SEQUENCE IF EXISTS public.heal_hospital_beds_history_ogc_fid_seq;
    
    -- create sequnce
    CREATE SEQUENCE IF NOT EXISTS public.heal_hospital_beds_history_ogc_fid_seq
        INCREMENT 1
        START 1
        MINVALUE 1
        MAXVALUE 9223372036854775807
        CACHE 1;
    
    
    -- grant sequnce
    ALTER TABLE IF EXISTS public.heal_hospital_beds_history_ogc_fid_seq OWNER to postgres;
    GRANT ALL ON TABLE public.heal_hospital_beds_history_ogc_fid_seq TO postgres WITH GRANT OPTION;
    
    -- create table
    CREATE TABLE IF NOT EXISTS public.heal_hospital_beds_history
    (
                data_time timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        name character varying(50) COLLATE pg_catalog."default",
        district character varying(50) COLLATE pg_catalog."default",
        addr character varying(50) COLLATE pg_catalog."default",
        phone character varying(50) COLLATE pg_catalog."default",
        acute_general_beds integer,
        acute_psychiatric_beds integer,
        chronic_general_beds integer,
        chronic_psychiatric_beds integer,
        palliative_beds integer,
        icu_beds integer,
        acute_respiratory_care_beds integer,
        chronic_respiratory_care_beds integer,
        burn_beds integer,
        emergency_observation_beds integer,
        other_observation_beds integer,
        surgical_recovery_beds integer,
        baby_beds integer,
        baby_sick_beds integer,
        hemodialysis_beds integer,
        peritoneal_dialysis_beds integer,
        psychiatric_icu_beds integer,
        burn_icu_beds integer,
        general_isolation_beds integer,
        positive_pressure_isolation_beds integer,
        negative_pressure_isolation_beds integer,
        bone_marrow_transplant_beds integer,
        lng double precision,
        lat double precision,
        wkb_geometry geometry(Point,4326),
        _ctime timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
        _mtime timestamp with time zone DEFAULT CURRENT_TIMESTAMP
            ,
        ogc_fid integer NOT NULL DEFAULT nextval('heal_hospital_beds_history_ogc_fid_seq'::regclass),
            
        CONSTRAINT heal_hospital_beds_history_pkey PRIMARY KEY (ogc_fid)
        
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    
    -- grant table
    ALTER TABLE IF EXISTS public.heal_hospital_beds_history OWNER to postgres;
    GRANT ALL ON TABLE public.heal_hospital_beds_history TO postgres WITH GRANT OPTION;
    
    
    -- create mtime trigger
    CREATE TRIGGER heal_hospital_beds_history_mtime
        BEFORE INSERT OR UPDATE 
        ON public.heal_hospital_beds_history
        FOR EACH ROW
        EXECUTE PROCEDURE public.trigger_set_timestamp();
    
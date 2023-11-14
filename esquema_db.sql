--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: agencias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.agencias (
    id integer NOT NULL,
    nombre character varying(255) NOT NULL,
    nivel character varying(50),
    ubicacion character varying(255)
);


ALTER TABLE public.agencias OWNER TO postgres;

--
-- Name: agencias_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.agencias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.agencias_id_seq OWNER TO postgres;

--
-- Name: agencias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.agencias_id_seq OWNED BY public.agencias.id;


--
-- Name: agentes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.agentes (
    id character varying(255) NOT NULL,
    nombre character varying(255) NOT NULL,
    agencia_id integer
);


ALTER TABLE public.agentes OWNER TO postgres;

--
-- Name: agentes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.agentes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.agentes_id_seq OWNER TO postgres;

--
-- Name: agentes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.agentes_id_seq OWNED BY public.agentes.id;


--
-- Name: clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes (
    id character varying(255) NOT NULL,
    nombre character varying(255) NOT NULL,
    informacion_contacto text,
    agente_id character varying(255)
);


ALTER TABLE public.clientes OWNER TO postgres;

--
-- Name: clientes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clientes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clientes_id_seq OWNER TO postgres;

--
-- Name: clientes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clientes_id_seq OWNED BY public.clientes.id;


--
-- Name: descuentos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.descuentos (
    id integer NOT NULL,
    descripcion character varying(255),
    semana integer,
    porcentaje_descuento numeric(5,2),
    prestamo_id character varying(255)
);


ALTER TABLE public.descuentos OWNER TO postgres;

--
-- Name: descuentos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.descuentos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.descuentos_id_seq OWNER TO postgres;

--
-- Name: descuentos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.descuentos_id_seq OWNED BY public.descuentos.id;


--
-- Name: pagos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pagos (
    id integer NOT NULL,
    monto numeric(12,2) NOT NULL,
    fecha_pago date NOT NULL,
    prestamo_id character varying(255),
    agente_id character varying(255),
    tarifa numeric(12,2)
);


ALTER TABLE public.pagos OWNER TO postgres;

--
-- Name: pagos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pagos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pagos_id_seq OWNER TO postgres;

--
-- Name: pagos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pagos_id_seq OWNED BY public.pagos.id;


--
-- Name: prestamos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prestamos (
    id character varying(255) NOT NULL,
    monto numeric(12,2),
    fecha_inicio date,
    estado character varying(50),
    cliente_id character varying(255),
    tarifa numeric(12,2),
    monto_otorgado numeric(12,2),
    cargo numeric(12,2),
    total_a_pagar numeric(12,2),
    primer_pago numeric(12,2),
    agente_id character varying(255)
);


ALTER TABLE public.prestamos OWNER TO postgres;

--
-- Name: prestamos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.prestamos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.prestamos_id_seq OWNER TO postgres;

--
-- Name: prestamos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.prestamos_id_seq OWNED BY public.prestamos.id;


--
-- Name: agencias id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agencias ALTER COLUMN id SET DEFAULT nextval('public.agencias_id_seq'::regclass);


--
-- Name: agentes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agentes ALTER COLUMN id SET DEFAULT nextval('public.agentes_id_seq'::regclass);


--
-- Name: clientes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes ALTER COLUMN id SET DEFAULT nextval('public.clientes_id_seq'::regclass);


--
-- Name: descuentos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.descuentos ALTER COLUMN id SET DEFAULT nextval('public.descuentos_id_seq'::regclass);


--
-- Name: pagos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagos ALTER COLUMN id SET DEFAULT nextval('public.pagos_id_seq'::regclass);


--
-- Name: prestamos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamos ALTER COLUMN id SET DEFAULT nextval('public.prestamos_id_seq'::regclass);


--
-- Name: agencias agencias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agencias
    ADD CONSTRAINT agencias_pkey PRIMARY KEY (id);


--
-- Name: agentes agentes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agentes
    ADD CONSTRAINT agentes_pkey PRIMARY KEY (id);


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


--
-- Name: descuentos descuentos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.descuentos
    ADD CONSTRAINT descuentos_pkey PRIMARY KEY (id);


--
-- Name: pagos pagos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagos
    ADD CONSTRAINT pagos_pkey PRIMARY KEY (id);


--
-- Name: prestamos prestamos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamos
    ADD CONSTRAINT prestamos_pkey PRIMARY KEY (id);


--
-- Name: agentes agentes_agencia_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agentes
    ADD CONSTRAINT agentes_agencia_id_fkey FOREIGN KEY (agencia_id) REFERENCES public.agencias(id);


--
-- Name: descuentos descuentos_prestamo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.descuentos
    ADD CONSTRAINT descuentos_prestamo_id_fkey FOREIGN KEY (prestamo_id) REFERENCES public.prestamos(id);


--
-- Name: pagos pagos_agente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagos
    ADD CONSTRAINT pagos_agente_id_fkey FOREIGN KEY (agente_id) REFERENCES public.agentes(id);


--
-- Name: pagos pagos_prestamo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagos
    ADD CONSTRAINT pagos_prestamo_id_fkey FOREIGN KEY (prestamo_id) REFERENCES public.prestamos(id);


--
-- Name: prestamos prestamos_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prestamos
    ADD CONSTRAINT prestamos_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES public.clientes(id);


--
-- PostgreSQL database dump complete
--


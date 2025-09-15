--
-- PostgreSQL database dump
--

\restrict WyS2Xh4AJCKGOcq345diuESA5U2mD9Ytguu7tUc7jrxfiQhOgkMhcHwksLUDg1L

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: complaint_history; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.complaint_history (
    id integer NOT NULL,
    complaint_id integer NOT NULL,
    status character varying(20) NOT NULL,
    remarks text,
    evidence_path character varying(255),
    changed_by integer,
    changed_at timestamp without time zone
);


ALTER TABLE public.complaint_history OWNER TO postgres;

--
-- Name: complaint_history_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.complaint_history_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.complaint_history_id_seq OWNER TO postgres;

--
-- Name: complaint_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.complaint_history_id_seq OWNED BY public.complaint_history.id;


--
-- Name: complaints; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.complaints (
    id integer NOT NULL,
    student_id integer NOT NULL,
    category character varying(100) NOT NULL,
    title character varying(200) NOT NULL,
    description text NOT NULL,
    evidence_path character varying(255),
    anonymous boolean,
    severity character varying(20),
    updates_email boolean,
    status character varying(20),
    assigned_teacher_id integer,
    deadline timestamp without time zone,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.complaints OWNER TO postgres;

--
-- Name: complaints_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.complaints_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.complaints_id_seq OWNER TO postgres;

--
-- Name: complaints_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.complaints_id_seq OWNED BY public.complaints.id;


--
-- Name: feedback; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.feedback (
    id integer NOT NULL,
    complaint_id integer NOT NULL,
    student_id integer NOT NULL,
    rating integer NOT NULL,
    comments text,
    created_at timestamp without time zone
);


ALTER TABLE public.feedback OWNER TO postgres;

--
-- Name: feedback_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.feedback_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.feedback_id_seq OWNER TO postgres;

--
-- Name: feedback_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.feedback_id_seq OWNED BY public.feedback.id;


--
-- Name: notifications; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notifications (
    id integer NOT NULL,
    user_id integer NOT NULL,
    message character varying(255) NOT NULL,
    is_read boolean,
    created_at timestamp without time zone
);


ALTER TABLE public.notifications OWNER TO postgres;

--
-- Name: notifications_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notifications_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.notifications_id_seq OWNER TO postgres;

--
-- Name: notifications_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notifications_id_seq OWNED BY public.notifications.id;


--
-- Name: teachers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teachers (
    id integer NOT NULL,
    category character varying(100) NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.teachers OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    email character varying(150) NOT NULL,
    password_hash character varying(255) NOT NULL,
    role character varying(20) NOT NULL,
    phone character varying(20) NOT NULL,
    department character varying(50) NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: complaint_history id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_history ALTER COLUMN id SET DEFAULT nextval('public.complaint_history_id_seq'::regclass);


--
-- Name: complaints id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaints ALTER COLUMN id SET DEFAULT nextval('public.complaints_id_seq'::regclass);


--
-- Name: feedback id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feedback ALTER COLUMN id SET DEFAULT nextval('public.feedback_id_seq'::regclass);


--
-- Name: notifications id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications ALTER COLUMN id SET DEFAULT nextval('public.notifications_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: complaint_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.complaint_history (id, complaint_id, status, remarks, evidence_path, changed_by, changed_at) FROM stdin;
1	9	Pending	Complaint submitted	\N	1	2025-09-14 18:06:04.349766
2	11	Resolved	Complaint resolved	\N	1	2025-09-14 18:10:10.505617
3	12	Pending	Complaint submitted	\N	1	2025-09-14 18:21:01.24233
\.


--
-- Data for Name: complaints; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.complaints (id, student_id, category, title, description, evidence_path, anonymous, severity, updates_email, status, assigned_teacher_id, deadline, created_at, updated_at) FROM stdin;
9	1	infrastructure	Sports Equipment	No sports equipment in the campus.	uploads/ac7d67dccefa478a8b66e039b49e0df2.jpg	f	Urgent	f	Pending	3	2025-09-16 18:06:04.291227	2025-09-14 18:06:04.291227	2025-09-14 18:06:04.310336
11	1	infrastructure	Hostel Issues	Water Leakage in hostel washroom.	uploads/50c665efc8614fa1a470164657a55218.jpg	t	Normal	f	Resolved	3	2025-09-19 18:10:10.465267	2025-09-14 18:10:10.465267	2025-09-14 18:10:10.48025
12	1	academic	Academic Issues	No proper study material	uploads/9d30ce0df3b3459bafc78f961eef161c.jpeg	f	Urgent	t	Pending	4	2025-09-16 18:21:01.120589	2025-09-14 18:21:01.120589	2025-09-14 18:21:01.177209
\.


--
-- Data for Name: feedback; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.feedback (id, complaint_id, student_id, rating, comments, created_at) FROM stdin;
2	9	2	5	Excellent resolution of the complaint	2025-09-15 03:16:41.553737
3	11	3	4	Very good solving of the complaint	2025-09-15 03:17:16.916669
\.


--
-- Data for Name: notifications; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notifications (id, user_id, message, is_read, created_at) FROM stdin;
1	1	Your complaint #9 has been submitted successfully.	f	2025-09-14 18:06:04.359495
2	1	Your complaint #11 has been submitted successfully.	f	2025-09-14 18:10:10.505617
3	1	Your complaint #12 has been submitted successfully.	f	2025-09-14 18:21:01.257052
\.


--
-- Data for Name: teachers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teachers (id, category, is_active) FROM stdin;
2	academic	t
3	infrastructure	t
4	academic	t
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, email, password_hash, role, phone, department, created_at) FROM stdin;
1	Harshita Chhabria	harshitachhabria18@gmail.com	scrypt:32768:8:1$9EEGqWFOVmXC1lJI$4848c0de8d686b01fc3cf00bab4fbb5afb63e95a4aa4b63dd0444d458d22da9b5fe59a933d054c3f6995f2d4e063dac8449be4710f857d9df0a7395c2658dc97	student	9016387023	B.Tech	2025-09-13 18:26:22.526831
2	Pawan Chhabria	pawan.chhabria@gmail.com	scrypt:32768:8:1$6jzwgfPQTPatFTuj$3e50610594122102967299e717632b40e1475056bc2f47693194a45a70cc966d5bbd1fcaf5cafc92519dba73315eefd9a3c49eeb02ab1c4bbbb8f3c297cd9c02	teacher	9099002365	BCA	2025-09-14 13:59:23.83378
3	Jyoti Chhabria	jyotichhabria@gmail.com	scrypt:32768:8:1$ErRs2OGr8BCBEFyg$2244f3e8f5a29980af48cb07a08d6e4305d3a5d7f0cd0d9eed6fa5d58ff2dac8268d152711a8605586eab2b67ef5df6ca53c7f2fdfbbb50ad36f4dfdff453e75	teacher	9922345672	BBA	2025-09-14 14:00:31.7612
4	Bhumika Chhabria	bhumikachhabria25@gmail.com	scrypt:32768:8:1$5cFyyoyHlLNitrYK$56ca8c88ca11e3ac100d72ce651ab39179232050f938765d420d6a9b72f5c2a584e3f43987fda0f27a8d0748a17540ad3c67d3b972ecd4f7ad940fd67d4c22b1	teacher	9510660337	MBA	2025-09-14 14:01:15.90894
5	Yashika Harwani	yashikaharwani123@gmail.com	scrypt:32768:8:1$OASXRoeZIOjqOpAP$bc6b31f3aadd2350636d30f71beb46befa70afd4dc984a73fc89187a54c0ee5dda2c9ca065c15eb4c6238dc077c1851f260b958dfaa0c1c24981c61be312dc3f	student	6354809787	B.Tech	2025-09-14 16:20:26.519261
6	Vanshika	vanshikaramchandani123@gmail.com	scrypt:32768:8:1$o5ZnGDy8YClwDQpd$2623ade35a2aad69494331e251f85b3052571403b6a31c545edca600bc2403bf80cadca77ef1678a2385642de029687a3c24243a7d2c8e287a1dfdddc245d90e	student	9510660356	MCA	2025-09-14 16:23:33.06704
\.


--
-- Name: complaint_history_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.complaint_history_id_seq', 3, true);


--
-- Name: complaints_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.complaints_id_seq', 12, true);


--
-- Name: feedback_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.feedback_id_seq', 3, true);


--
-- Name: notifications_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notifications_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 6, true);


--
-- Name: complaint_history complaint_history_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_history
    ADD CONSTRAINT complaint_history_pkey PRIMARY KEY (id);


--
-- Name: complaints complaints_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaints
    ADD CONSTRAINT complaints_pkey PRIMARY KEY (id);


--
-- Name: feedback feedback_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT feedback_pkey PRIMARY KEY (id);


--
-- Name: notifications notifications_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_pkey PRIMARY KEY (id);


--
-- Name: teachers teachers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: complaint_history complaint_history_changed_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_history
    ADD CONSTRAINT complaint_history_changed_by_fkey FOREIGN KEY (changed_by) REFERENCES public.users(id);


--
-- Name: complaint_history complaint_history_complaint_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_history
    ADD CONSTRAINT complaint_history_complaint_id_fkey FOREIGN KEY (complaint_id) REFERENCES public.complaints(id);


--
-- Name: complaints complaints_assigned_teacher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaints
    ADD CONSTRAINT complaints_assigned_teacher_id_fkey FOREIGN KEY (assigned_teacher_id) REFERENCES public.teachers(id);


--
-- Name: complaints complaints_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaints
    ADD CONSTRAINT complaints_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.users(id);


--
-- Name: feedback feedback_complaint_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT feedback_complaint_id_fkey FOREIGN KEY (complaint_id) REFERENCES public.complaints(id);


--
-- Name: feedback feedback_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT feedback_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.users(id);


--
-- Name: notifications notifications_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: teachers teachers_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_id_fkey FOREIGN KEY (id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

\unrestrict WyS2Xh4AJCKGOcq345diuESA5U2mD9Ytguu7tUc7jrxfiQhOgkMhcHwksLUDg1L


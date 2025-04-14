CREATE TABLE oac_tw_table (
    loc INT,
    loc_zn VARCHAR(255),
    loc_name VARCHAR(255),
    loc_purp_desc VARCHAR(2),
    loc_qti VARCHAR(3),
    flow_ind VARCHAR(1),
    dc Float,
    opc INT,
    tsq INT,
    oac INT,
    it BOOLEAN,
    auth_overrun_ind BOOLEAN,
    nom_cap_exceed_ind BOOLEAN,
    all_qty_avail BOOLEAN,
    qty_reason VARCHAR(255),
    gas_day DATE,
    cycle INT
);
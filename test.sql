INSERT INTO flo_settlement_test_integration.settlement_result (service_date, settlement_month, delivered_global_id,
            translated_global_id, track_hits_for_service_id, daily_subscriber, track_hits_rate_for_service_id,
            settlement_target_amount_per_day, neighboring_copyright_rate_fee, neighboring_copyright_unit_fee,
            neighboring_copyright_daily_subscriber_fee, neighboring_copyright_fee, copyright_rate_fee,
            copyright_unit_fee, copyright_daily_subscriber_fee, copyright_fee, play_right_rate_fee, play_right_unit_fee,
            play_right_daily_subscriber_fee, play_right_fee, total_settlement_amount, settlement_profit, sales_share,
            total_hits_for_service_id, daily_subscriber_per_service_id, neighboring_copyright_rate,
            neighboring_copyright_unit_price, neighboring_copyright_subscriber, right_holder_id, right_holder_name,
            contract_id, contract_name, calculation_id, calculation_name, sales_channel, settlement_type, pass_type,
            single_multi, major_classification, medium_classification, minor_classification, levy_rule_version,
            levy_rule_id, levy_rule_name, service_id, service_id_name, delivered_local_id, album_id, album_name,
            album_artist_name, upc, right_holder_album_id, track_id, track_name, uci, isrc, right_holder_track_id,
            artist_id, artist_name, agency_id, agency_name, album_issue_date, contents_name, type, yyyymmdd,
            settlement_yyyymm)
        WITH
        sfl AS (
            SELECT
                *,
                split_part(delivered_global_id, '/', 1) AS delivered_meta_type,
                cast(split_part(delivered_global_id, '/', 2) AS bigint) AS delivered_local_no,
                split_part(translated_global_id, '/', 1) AS translated_meta_type,
                cast(split_part(translated_global_id, '/', 2) AS bigint) AS translated_local_no
            FROM (SELECT * FROM flo_settlement_test_integration.settlement_log_finance WHERE yyyymmdd = '20220228')
        )
        SELECT
            timestamp '2022-02-28' AS service_date,
            timestamp '2022-03-01 00:00:00' AS settlement_month,
            sfl.delivered_global_id,
            sfl.translated_global_id,
            sfl.track_hits_for_service_id,
            sfl.daily_subscriber,
            sfl.track_hits_rate_for_service_id,
            sfl.settlement_target_amount_per_day,
            sfl.neighboring_copyright_rate_fee,
            sfl.neighboring_copyright_unit_fee,
            sfl.neighboring_copyright_daily_subscriber_fee,
            sfl.neighboring_copyright_fee,
            sfl.copyright_rate_fee,
            sfl.copyright_unit_fee,
            sfl.copyright_daily_subscriber_fee,
            sfl.copyright_fee,
            sfl.play_right_rate_fee,
            sfl.play_right_unit_fee,
            sfl.play_right_daily_subscriber_fee,
            sfl.play_right_fee,
            sfl.total_settlement_amount,
            sfl.settlement_profit,
            sfl.sales_share,
            sfl.total_hits_for_service_id,
            sfl.daily_subscriber_per_service_id,
            sfl.neighboring_copyright_rate,
            sfl.neighboring_copyright_unit_price,
            sfl.neighboring_copyright_subscriber,
            sfl.right_holder_id AS right_holder_id,
            rh.rh_name AS right_holder_name,
            sfl.contract_id,
            rhc.contract_name AS contract_name,
            ci.ca_id AS calculation_id,
            ci.ca_id_name AS calculation_name,
            sc.poc AS sales_channel,
            ci.charge_type AS settlement_type,
            ci.pass_sale_type AS pass_type,
            ci.product_type AS single_multi,
            ci.category_type1 AS major_classification,
            ci.category_type2 AS medium_classification,
            ci.category_type3 AS minor_classification,
            ci.levy_rule_version AS levy_rule_version,
            ci.levy_rule_cd AS levy_rule_id,
            ci.levy_rule_name AS levy_rule_name,
            sfl.service_id,
            si.svc_id_name AS service_id_name,
            CAST(delivered_local_no AS varchar) AS delivered_local_id,
            al.album_id AS album_id,

        IF(al.display_title_use_yn = 'Y',
            al.album_display_title,
            al.album_title  || if(al.album_sub_title != '', ' (' || al.album_sub_title || ')', '') || if(al.album_version != '', ' (' || al.album_version || ')', ''))
     AS album_name,
            aar.artist_name AS album_artist_name,
            al.upc,
            anr.ch_album_cd AS right_holder_album_id,
            translated_local_no AS track_id,
            CASE translated_meta_type
                WHEN 'TRACK' THEN
        IF(t.display_title_use_yn = 'Y',
            t.track_display_title,
            t.track_title  || if(t.track_version != '', ' (' || t.track_version || ')', '') || if(t.add_info != '', ' (' || t.add_info || ')', ''))

                WHEN 'VCOLORING' THEN vc.title
            END AS track_name,
            t.uci,
            t.isrc,
            CASE translated_meta_type
                WHEN 'TRACK' THEN tnr.ch_track_cd
                WHEN 'VCOLORING' THEN vc.ch_vc_cd
            END AS right_holder_track_id,
            tar.artist_id AS artist_id,
            CASE translated_meta_type
                WHEN 'TRACK' THEN tar.artist_name
                WHEN 'VCOLORING' THEN vc.display_artist_name
            END AS artist_name,
            coalesce(tag.agency_id, aag.agency_id) AS agency_id,
            coalesce(tag.agency_name, aag.agency_name, t.label_company) AS agency_name,
            al.album_issue_date,
            vc.title AS contents_name,
            'DailySettlement' AS type,
            '20220228' AS yyyymmdd,
            '202203' AS settlement_yyyymm
        FROM sfl
            LEFT OUTER JOIN (SELECT * FROM flo_settlement_meta.tnmm_track WHERE yyyymmdd = '20220201') t ON translated_meta_type = 'TRACK' AND t.track_id = translated_local_no
            LEFT OUTER JOIN (
        SELECT *
        FROM (SELECT * FROM flo_settlement_meta.tnmm_track_nr WHERE yyyymmdd = '20220201')
        WHERE cast(rights_start_dt AS date) <= timestamp '2022-02-28 00:00:00'
            AND timestamp '2022-02-28 23:59:59' <= rights_end_dt
    ) tnr ON tnr.track_id = t.track_id
            LEFT OUTER JOIN (SELECT * FROM flo_settlement_meta.tmcr_rights_holder WHERE yyyymmdd = '20220201') rh ON rh.rh_id = sfl.right_holder_id
            LEFT OUTER JOIN (SELECT * FROM flo_settlement_meta.tncr_svc_id WHERE yyyymmdd = '20220201') si ON si.svc_id = sfl.service_id
            LEFT OUTER JOIN (SELECT * FROM flo_settlement_meta.tncr_ca_id WHERE yyyymmdd = '20220201') ci ON ci.ca_id = si.ca_id
            LEFT OUTER JOIN (SELECT * FROM flo_settlement_meta.tncr_sale_channel WHERE yyyymmdd = '20220201') sc ON sc.ca_id = ci.ca_id
            LEFT OUTER JOIN (SELECT * FROM flo_settlement_meta.tnmm_album WHERE yyyymmdd = '20220201') al ON translated_meta_type = 'TRACK' AND al.album_id = t.album_id
            LEFT OUTER JOIN (
        SELECT *
        FROM (SELECT * FROM flo_settlement_meta.tnmm_album_nr WHERE yyyymmdd = '20220201')
        WHERE cast(rights_start_dt AS date) <= timestamp '2022-02-28 00:00:00'
            AND timestamp '2022-02-28 23:59:59' <= rights_end_dt
    ) anr ON anr.album_id = al.album_id
            LEFT OUTER JOIN (
                SELECT album_id, array_join(array_distinct(array_agg(artist_name ORDER BY coalesce(sort_order, 9999), artist_no)), ',') AS artist_name
                FROM (
                    SELECT aa.album_id, aa.artist_no, aa.sort_order, aa.artist_id, aar.artist_name
                    FROM (SELECT * FROM flo_settlement_meta.tnmm_album_artist WHERE yyyymmdd = '20220201') aa
                        INNER JOIN (SELECT * FROM flo_settlement_meta.tnmm_artist WHERE yyyymmdd = '20220201') aar ON aar.artist_id = aa.artist_id
                ) dd
                GROUP BY album_id
            ) aar ON translated_meta_type = 'TRACK' AND aar.album_id = t.album_id
            LEFT OUTER JOIN (
        SELECT track_id,
            array_join(array_distinct(array_agg(cast(artist_id AS varchar) ORDER BY coalesce(sort_order, 9999), artist_no)), ',') AS artist_id,
            array_join(array_distinct(array_agg(artist_name ORDER BY sort_order, artist_id)), ',') AS artist_name
        FROM (
            SELECT ta.track_id, ta.artist_no, ta.sort_order, ta.artist_id, tar.artist_name
            FROM (SELECT * FROM flo_settlement_meta.tnmm_track_artist WHERE yyyymmdd = '20220201') ta
                INNER JOIN (SELECT * FROM flo_settlement_meta.tnmm_artist WHERE yyyymmdd = '20220201') tar ON tar.artist_id = ta.artist_id
        ) ee
        GROUP BY track_id
    ) tar ON translated_meta_type = 'TRACK' AND tar.track_id = t.track_id
            LEFT OUTER JOIN (
                SELECT track_id,
                    array_join(array_distinct(array_agg(cast(agency_id AS varchar) ORDER BY sort_order)), ',') AS agency_id,
                    array_join(array_distinct(array_agg(agency_nm ORDER BY sort_order)), ',') AS agency_name
                FROM (
                    SELECT tag.track_id, tag.sort_order, ag.agency_id, ag.agency_nm
                    FROM (SELECT * FROM flo_settlement_meta.tnmm_track_agency WHERE yyyymmdd = '20220201') tag
                        INNER JOIN (SELECT * FROM flo_settlement_meta.tmcr_agency WHERE yyyymmdd = '20220201') ag ON ag.agency_id = tag.agency_id
                ) ff
                GROUP BY track_id
            ) tag ON translated_meta_type = 'TRACK' AND tag.track_id = t.track_id
            LEFT OUTER JOIN (
                SELECT album_id,
                    array_join(array_distinct(array_agg(cast(agency_id AS varchar) ORDER BY sort_order)), ',') AS agency_id,
                    array_join(array_distinct(array_agg(agency_nm ORDER BY sort_order)), ',') AS agency_name
                FROM (
                    SELECT aag.album_id, aag.sort_order, ag.agency_id, ag.agency_nm
                    FROM (SELECT * FROM flo_settlement_meta.tnmm_album_agency WHERE yyyymmdd = '20220201') aag
                        INNER JOIN (SELECT * FROM flo_settlement_meta.tmcr_agency WHERE yyyymmdd = '20220201') ag ON ag.agency_id = aag.agency_id
                ) ff
                GROUP BY album_id
            ) aag ON translated_meta_type = 'TRACK' AND aag.album_id = t.album_id
            LEFT OUTER JOIN (SELECT * FROM flo_settlement_meta.tncr_rh_contract WHERE yyyymmdd = '20220201') rhc ON rhc.contract_id = sfl.contract_id
            LEFT OUTER JOIN (SELECT * FROM flo_settlement_meta.tnvc_vcoloring WHERE yyyymmdd = '20220201') vc ON delivered_meta_type = 'VCOLORING' AND vc.vc_id = delivered_local_no



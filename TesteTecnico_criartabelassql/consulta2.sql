SELECT 
    o.Razao_Social,
    o.Nome_Fantasia,
    SUM(s.valor_despesa) AS total_despesas
FROM 
    operadoras o
JOIN 
    sinistros s ON o.Registro_ANS = s.registro_ans
WHERE 
    s.tipo_evento = 'ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND s.data_evento BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 3 MONTH) AND CURRENT_DATE()
GROUP BY 
    o.Razao_Social, o.Nome_Fantasia
ORDER BY 
    total_despesas DESC
LIMIT 10;
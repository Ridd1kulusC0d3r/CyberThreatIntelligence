-- SQLite: >=3 falhas da mesma conta/IP/cliente, nos 5 minutos anteriores ao sucesso.
-- Janela inclusiva em -300 s e exclusiva no instante do sucesso.
SELECT s.event_id, s.tenant, s.account, s.src_ip, COUNT(f.event_id) AS failures
FROM events s
JOIN events f ON f.tenant=s.tenant AND f.account=s.account AND f.src_ip=s.src_ip
  AND f.outcome='failure'
  AND unixepoch(f.ts) >= unixepoch(s.ts)-300
  AND unixepoch(f.ts) < unixepoch(s.ts)
WHERE s.outcome='success'
GROUP BY s.event_id,s.tenant,s.account,s.src_ip
HAVING COUNT(f.event_id)>=3
ORDER BY s.event_id;

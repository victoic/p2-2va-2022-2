## Documentação do protocolo de comunicação server - client

### On `log_server`
**Shoot**
`SHOOT player_id targetX targetY`

**Start** 
`START player_id`

**Result**
`RESULT player_id targetX targetY value`

**End Game**
`ENDGAME`

---

### On `log_player`
**Shoot**
`SHOOT targetX targetY`

**Result**
`RESULT targetX targetY value`
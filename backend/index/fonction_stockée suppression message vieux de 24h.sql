CREATE OR REPLACE FUNCTION delete_old_msg_on_channelsMessage()
RETURNS void AS $$
BEGIN
  DELETE FROM "channelsMessage"
  WHERE date < NOW() - INTERVAL '24 hours';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION trigger_delete_old_records_on_channelsMessage()
RETURNS TRIGGER AS $$
BEGIN
  PERFORM delete_old_msg_on_channelsMessage();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER delete_old_records_trigger_on_channelsMessage
AFTER INSERT OR UPDATE ON "channelsMessage"
EXECUTE FUNCTION trigger_delete_old_records_on_channelsMessage();
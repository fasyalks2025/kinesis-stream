%flink.ssql -- NOTE: this is necessary in apache zeppelin
CREATE TABLE sensor_data_table (
  sensor_id INT,
  temperature DOUBLE,
  humidity DOUBLE,
  event_time BIGINT
)

WITH (
  'connector' = 'kinesis',
  'stream' = 'SensorDataStream', -- NOTE: change this to your kinesis stream name 
  'aws.region' = 'ap-southeast-1', -- NOTE: change this according to your region
  'scan.stream.initpos' = 'LATEST',
  'format' = 'json'
);

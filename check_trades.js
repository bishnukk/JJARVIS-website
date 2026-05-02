
const { createClient } = require('@supabase/supabase-js');
const SUPABASE_URL = 'https://hlfianhpyryrnnmxwlcy.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsZmlhbmhweXJ5cm5ubXh3bGN5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYzMTc5MjIsImV4cCI6MjA5MTg5MzkyMn0.SeCgt7JYkYpKmjWSAYBlkLOuE5cL7HkvvjD02WGk4Ik';
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

async function check() {
  const { data, error } = await supabase.from('orders').select('jr_trade_id');
  if (error) console.error(error);
  else {
    const ids = data.map(d => d.jr_trade_id);
    const unique = new Set(ids);
    console.log('Total rows:', data.length);
    console.log('Unique trade IDs:', unique.size);
  }
}
check();


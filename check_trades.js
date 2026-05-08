
const { createClient } = require('@supabase/supabase-js');
const SUPABASE_URL = 'https://hlfianhpyryrnnmxwlcy.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsZmlhbmhweXJ5cm5ubXh3bGN5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYzMTc5MjIsImV4cCI6MjA5MTg5MzkyMn0.SeCgt7JYkYpKmjWSAYBlkLOuE5cL7HkvvjD02WGk4Ik';
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

async function check() {
  console.log('--- Checking Signals ---');
  const { data: signals, error: sErr } = await supabase.from('signals').select('*').order('created_at', { ascending: false }).limit(5);
  if (sErr) console.error(sErr);
  else {
    console.log('Signals (last 5):');
    if (!signals || signals.length === 0) console.log('  No signals found.');
    else signals.forEach(s => console.log(`  ID: ${s.id}, Created: ${s.created_at}, Symbol: ${s.symbol}, Status: ${s.status}`));
  }

  console.log('\n--- Checking Orders ---');
  const { data: orders, error: oErr } = await supabase.from('orders').select('*').order('order_date', { ascending: false }).limit(10);
  if (oErr) console.error(oErr);
  else {
    console.log('Orders (last 10):');
    if (!orders || orders.length === 0) console.log('  No orders found.');
    else orders.forEach(o => {
        console.log(`  ID: ${o.id}, TID: ${o.jr_trade_id}, Date: ${o.order_date}, Created: ${o.created_at}, Pair: ${o.jr_pair}, Status: ${o.status}`);
    });
  }
}
check();

-- Check RLS policies for shops table
SELECT *
FROM pg_policies
WHERE tablename = 'shops';

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6f57c820-6b74-4efe-9fa0-f44cabc36f8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Done! Created stop_mapping.csv with 4228 unique stops.\n",
      "Sample stops created: ['stop id from                                                  386\\nstop id to                                                  38709\\ntrip id                 323 Ma Na Pa', 'stop id from                                                          437\\nstop id to                                                            442\\ntrip id                 152 MNP', 'stop id from                                                          440\\nstop id to                                                          38702\\ntrip id                 152 MNP', 'stop id from                                                          441\\nstop id to                                                            440\\ntrip id                 152 MNP', 'stop id from                                                          442\\nstop id to                                                          38699\\ntrip id                 152 MNP', 'stop id from                                                          447\\nstop id to                                                          38710\\ntrip id                 152 MNP', 'stop id from                                                          460\\nstop id to                                                          38755\\ntrip id                 VJR4 Kothrud Depot', 'stop id from                                                          461\\nstop id to                                                            526\\ntrip id                 152 MNP', 'stop id from                                                    467\\nstop id to                                                    39187\\ntrip id                 5 Swargate', 'stop id from                                                     469\\nstop id to                                                     39225\\ntrip id                 103 Katraj']\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import re\n",
    "\n",
    "# Load your main data\n",
    "df = pd.read_csv('GTFS_Data.csv')\n",
    "\n",
    "def extract_clean_names(trip_id):\n",
    "    # Removes \"NORMAL_\", \"Up/Down\", and \"Time\" to get the route names\n",
    "    clean = re.sub(r'NORMAL_|_[0-9]+|Up|Down|-[0-9]+', '', str(trip_id))\n",
    "    clean = clean.replace('_', ' ').strip()\n",
    "    # Usually format is \"A To B\"\n",
    "    if \" To \" in clean:\n",
    "        parts = clean.split(\" To \")\n",
    "        return parts[0].strip(), parts[1].strip()\n",
    "    return clean, clean\n",
    "\n",
    "# Extract names\n",
    "names = df.apply(extract_clean_names, axis=1)\n",
    "df['start_name'] = [n[0] for n in names]\n",
    "\n",
    "# Create the mapping: For every ID, find the most common name assigned to it\n",
    "mapping = df.groupby('stop_id_from')['start_name'].agg(lambda x: x.value_counts().index[0]).reset_index()\n",
    "mapping.columns = ['stop_id', 'stop_name']\n",
    "\n",
    "# Save it\n",
    "mapping.to_csv('stop_mapping.csv', index=False)\n",
    "print(f\"Done! Created stop_mapping.csv with {len(mapping)} unique stops.\")\n",
    "print(\"Sample stops created:\", mapping['stop_name'].head(10).tolist())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93dabebf-18f6-4948-a35f-bd62620f0dfd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

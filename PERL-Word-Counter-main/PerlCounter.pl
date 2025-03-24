#!/usr/bin/perl
use strict;
use warnings;

# Get input text
my $text = @ARGV ? join(' ', @ARGV) : do {
    print "Enter text: ";
    my $input = <STDIN>;
    chomp($input);
    $input;
};

# Convert to lowercase and remove punctuation
$text = lc($text);
$text =~ s/[^\w\s]//g;

# Count word occurrences
my %word_count;
foreach my $word (split(/\s+/, $text)) {
    next if $word eq '';
    $word_count{$word}++;
}

# Find the most frequent word(s)
my $max_count = 0;
my @most_frequent;

foreach my $word (keys %word_count) {
    if ($word_count{$word} > $max_count) {
        $max_count = $word_count{$word};
        @most_frequent = ($word);
    } 
    elsif ($word_count{$word} == $max_count) {
        push @most_frequent, $word;
    }
}

# Print results
print "\nResults:\n";
print "Most frequent word(s): ", join(", ", @most_frequent), "\n";
print "Occurrences: $max_count\n\n";

# Print word frequency table
print "Word | Count\n";
print "-" x 15, "\n";
foreach my $word (sort { $word_count{$b} <=> $word_count{$a} } keys %word_count) {
    printf "%-10s | %d\n", $word, $word_count{$word};
}

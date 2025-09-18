'use client';

import React, { useState } from 'react';
import { User, Mail, Phone, MapPin, Calendar, Building } from 'lucide-react';

interface UserProfile {
  id: number;
  name: string;
  email: string;
  phone: string;
  location: string;
  company: string;
  role: string;
  joinDate: string;
  avatar: string;
  bio: string;
}

export default function UserProfilesPage() {
  const [selectedProfile, setSelectedProfile] = useState<UserProfile | null>(null);

  const users: UserProfile[] = [
    {
      id: 1,
      name: "Michael Chen",
      email: "michael.chen@email.com",
      phone: "+1 (555) 987-6543",
      location: "Seattle, WA",
      company: "Design Studio",
      role: "UX Designer",
      joinDate: "January 2023",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face",
      bio: "Creative designer focused on creating intuitive and beautiful user experiences."
    },
    {
      id: 2,
      name: "Emily Rodriguez",
      email: "emily.rodriguez@email.com",
      phone: "+1 (555) 456-7890",
      location: "Austin, TX",
      company: "Marketing Pro",
      role: "Marketing Manager",
      joinDate: "September 2021",
      avatar: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face",
      bio: "Data-driven marketing professional specializing in digital campaigns and brand strategy."
    },
    {
      id: 3,
      name: "David Kim",
      email: "david.kim@email.com",
      phone: "+1 (555) 321-0987",
      location: "New York, NY",
      company: "Finance Corp",
      role: "Financial Analyst",
      joinDate: "June 2020",
      avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face",
      bio: "Experienced analyst with expertise in financial modeling and investment strategies."
    }
  ];

  const ProfileCard = ({
    user,
    onClick,
    isSelected
  }: {
    user: UserProfile;
    onClick: (user: UserProfile) => void;
    isSelected: boolean;
  }) => (
    <div
      className={`bg-white rounded-xl shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer border-2 ${isSelected ? 'border-blue-500 shadow-xl' : 'border-transparent hover:border-gray-200'
        }`}
      onClick={() => onClick(user)}
    >
      <div className="p-6">
        <div className="flex items-center space-x-4">
          <img
            src={user.avatar}
            alt={user.name}
            className="w-16 h-16 rounded-full object-cover border-2 border-gray-100"
          />
          <div className="flex-1">
            <h3 className="text-xl font-semibold text-gray-900">{user.name}</h3>
            <p className="text-gray-600">{user.role}</p>
            <p className="text-sm text-gray-500">{user.company}</p>
          </div>
        </div>
      </div>
    </div>
  );

  const ProfileDetails = ({
    user,
    onClose
  }: {
    user: UserProfile;
    onClose: () => void;
  }) => (
    <div className="bg-white rounded-xl shadow-lg border border-gray-200">
      <div className="p-6 border-b border-gray-200">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <img
              src={user.avatar}
              alt={user.name}
              className="w-20 h-20 rounded-full object-cover border-3 border-blue-100"
            />
            <div>
              <h2 className="text-2xl font-bold text-gray-900">{user.name}</h2>
              <p className="text-lg text-blue-600 font-medium">{user.role}</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 text-2xl font-bold"
            aria-label="Close profile details"
          >
            ×
          </button>
        </div>
      </div>

      <div className="p-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="space-y-4">
            <div className="flex items-center space-x-3">
              <Mail className="w-5 h-5 text-gray-500" />
              <span className="text-gray-700">{user.email}</span>
            </div>
            <div className="flex items-center space-x-3">
              <Phone className="w-5 h-5 text-gray-500" />
              <span className="text-gray-700">{user.phone}</span>
            </div>
            <div className="flex items-center space-x-3">
              <MapPin className="w-5 h-5 text-gray-500" />
              <span className="text-gray-700">{user.location}</span>
            </div>
          </div>

          <div className="space-y-4">
            <div className="flex items-center space-x-3">
              <Building className="w-5 h-5 text-gray-500" />
              <span className="text-gray-700">{user.company}</span>
            </div>
            <div className="flex items-center space-x-3">
              <Calendar className="w-5 h-5 text-gray-500" />
              <span className="text-gray-700">Joined {user.joinDate}</span>
            </div>
          </div>
        </div>

        <div className="mt-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-2">About</h3>
          <p className="text-gray-700 leading-relaxed">{user.bio}</p>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">User Profiles</h1>
          <p className="text-gray-600">Click on any profile to view detailed information</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Profiles List */}
          <div className="space-y-4">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4 flex items-center">
              <User className="w-6 h-6 mr-2 text-blue-600" />
              Team Members
            </h2>
            {users.map((user) => (
              <ProfileCard
                key={user.id}
                user={user}
                onClick={setSelectedProfile}
                isSelected={selectedProfile?.id === user.id}
              />
            ))}
          </div>

          {/* Profile Details */}
          <div className="lg:sticky lg:top-4 h-fit">
            {selectedProfile ? (
              <ProfileDetails
                user={selectedProfile}
                onClose={() => setSelectedProfile(null)}
              />
            ) : (
              <div className="bg-white rounded-xl shadow-lg border border-gray-200 p-8 text-center">
                <User className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                <h3 className="text-xl font-semibold text-gray-600 mb-2">
                  Select a Profile
                </h3>
                <p className="text-gray-500">
                  Choose a team member from the list to view their detailed information
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}